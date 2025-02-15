Title: Ideas from "A Philosophy of Software Design"

URL Source: https://www.16elt.com/2024/09/25/first-book-of-byte-sized-tech/index.html

Published Time: 2024-09-25T15:30:46.000Z

Markdown Content:
Ideas from "A Philosophy of Software Design"
ELIRAN TURGEMAN 2024-09-25   books, byte-sized tech, software design  13 minutes

Almost a month ago, I created a telegram channel with the goal of reading tech books consistently, and sharing summaries of them.
This week, I have finished reading the first book - “A Philosophy of Software Design” by John Ousterhout and shared all of the 21 chapter summaries in the channel.

In this post, I will share what are the 3 ideas that resonated with me the most.
The book is pretty packed with insights, and I think many junior-mid level software engineers can benefit from them, so I do encourage you to read it yourself!

Idea 1: Zero-tolerance towards complexity

On the second chapter of the book, the author describes what is complexity and what are its symptoms:

Change amplification: a simple change requires changes in many different places.
Cognitive load: the developer needs to learn a lot to complete a task.
Unknown unknowns: it is not obvious which pieces of code need to change to complete a task.

The author argues that complexity is not caused by a single error, it accumulates. Sometimes we convince ourselves that a bit of complexity here won’t matter much, but if everyone on the project adopts this mindset, the project will become complex rapidly.

“In order to slow the growth of complexity, you must adopt a zero-tolerance philosophy”.

Example

Imagine a simple order processing system where you calculate shipping costs, and apply discounts. However, this system is poorly designed with duplicated logic across multiple services, leading to change amplification. Let’s say both the CheckoutService and the ShippingService use the same logic to calculate discounts, but it’s implemented separately in both places.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31

	
public class CheckoutService
{
    public decimal CalculateTotal(Order order)
    {
        decimal total = order.Items.Sum(item => item.Price);

        // Apply discount logic
        if (order.CouponCode == "SUMMER2024")
        {
            total -= 10;
        }

        return total;
    }
}

public class ShippingService
{
    public decimal CalculateShipping(Order order)
    {
        decimal shippingCost = order.ShippingAddress.Country == "US" ? 5 : 15;

        // Apply discount logic (duplicated)
        if (order.CouponCode == "SUMMER2024")
        {
            shippingCost -= 10;
        }

        return shippingCost;
    }
}

Why is it bad?

Change Amplification: If you want to modify how discounts are applied (e.g., introduce a new discount or change the criteria), you have to modify both CheckoutService and ShippingService.

Cognitive Load: Developers must remember to update every part of the system that touches discounts. Forgetting to update one part (e.g., missing it in ShippingService) will lead to inconsistent behavior.

Unknown Unknowns: If a new developer is tasked with updating the discount logic, they may not know that the same discount logic exists in multiple places. They might update one but miss the other, causing a bug in shipping cost calculations.

How to improve it?

We can refactor the system to eliminate duplicated logic by encapsulating the discount logic in its own class. This way, if the discount logic changes, you only need to modify one place, reducing overall complexity.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51

	
public class DiscountService
{
    public decimal ApplyDiscount(Order order, decimal total)
    {
        if (order.CouponCode == "SUMMER2024")
        {
            return total - 10;
        }
        return total;
    }
}

public class CheckoutService
{
    private readonly DiscountService _discountService;

    public CheckoutService(DiscountService discountService)
    {
        _discountService = discountService;
    }

    public decimal CalculateTotal(Order order)
    {
        decimal total = order.Items.Sum(item => item.Price);

        // Apply discount through centralized service
        total = _discountService.ApplyDiscount(order, total);

        return total;
    }
}

public class ShippingService
{
    private readonly DiscountService _discountService;

    public ShippingService(DiscountService discountService)
    {
        _discountService = discountService;
    }

    public decimal CalculateShipping(Order order)
    {
        decimal shippingCost = order.ShippingAddress.Country == "US" ? 5 : 15;

        // Apply discount through centralized service
        shippingCost = _discountService.ApplyDiscount(order, shippingCost);

        return shippingCost;
    }
}


To summarize, in the first example, we saw change amplification where a simple change to discount logic required modifying multiple services. By centralizing the logic in DiscountService, we eliminate this duplication, making it easier to maintain and evolve the system.

Idea 2: Smaller components are not necessarily better for modularity

“Given two pieces of functionality, should they be implemented together, or should their implementations be separated?” - This question was chapter’s 9 focus.

The author argues, while keeping in mind reducing the system’s complexity is our goal, that smaller components are not necessarily better for modularity, and mentions a few cons of splitting out functionality across more components:

“Some complexity comes just from the number of components”
“Subdivision can result in additional code to manage the components”
“Separation makes it harder for developers to see the components at the same time, or even to be aware of their existence.”
“Subdivision can result in duplication”

The author also offers a few indications that two pieces of code should be merged.

“They share information.”
“They are used together”, this has to be bidirectional. For example, if whenever I use method A, I always use method B and vice versa, then the methods should be merged.
“They overlap conceptually, in that there is a simple higher-level category that includes both of the pieces of code”
“It is hard to understand one of the pieces of code without looking at the other.”

The author mentions the common “clean tip”: “Split up any method longer than X lines.” He adds that “length by itself is rarely a good reason for splitting up a method.” […] Splitting up a method introduces additional interfaces, which add to complexity. […] You shouldn’t break up a method unless it makes the overall system simpler”.

Example

In this example, let’s say we have a user registration process in a system. The developer has over-split the logic into multiple methods, separating each step of the registration, such as validating the user, saving the user to the database, and sending a welcome email. While each method is doing its own thing, they all share information and are conceptually related. This over-splitting leads to unnecessary complexity and overhead.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30

	
public class UserService
{
    public bool ValidateUser(User user)
    {
        if (string.IsNullOrEmpty(user.Email))
        {
            throw new ArgumentException("Email is required.");
        }
        return true;
    }

    public void SaveUserToDatabase(User user)
    {
        Database.Save(user);
    }

    public void SendWelcomeEmail(User user)
    {
        EmailService.Send("Welcome to our platform!", user.Email);
    }

    public void RegisterUser(User user)
    {
        if (ValidateUser(user))
        {
            SaveUserToDatabase(user);
            SendWelcomeEmail(user);
        }
    }
}

Why is it bad?

Unnecessary Subdivision: The ValidateUser, SaveUserToDatabase, and SendWelcomeEmail methods are too granular and are always used together in a strict sequence. Splitting these steps adds unnecessary interfaces to the system without offering any real flexibility.

Increased Cognitive Load: The developer now has to mentally track multiple methods, which are tightly related but unnecessarily split apart. This subdivision introduces unnecessary complexity in understanding the registration process.

Information Overlap: All three methods are directly related to the user registration process. They share the same user object and are always invoked together. It’s hard to reason about one step in the process without considering the others.

How to improve it?

Simple, in that case we simply can “inline” the methods, like the following

1
2
3
4
5
6
7
8
9
10
11
12
13
14

	
public class UserService
{
    public void RegisterUser(User user)
    {
        if (string.IsNullOrEmpty(user.Email))
        {
            throw new ArgumentException("Email is required.");
        }

        Database.Save(user);

        EmailService.Send("Welcome to our platform!", user.Email);
    }
}


To summarize, splitting up functionality just for the sake of making smaller methods can actually add complexity, as shown in the first example. By merging related steps that share information and are always used together, we reduce subdivision overhead, simplify the interface, and make the code easier to understand and maintain.

Idea 3: Exception handling accounts for a lot of complexity

In chapter 10 the author argues that “Exception handling is one of the worst sources of complexity in software systems.”.

There are two ways to handle exceptions:

Try to complete the work in progress (i.e., network packet lost? Resend; data corrupted? Recover from snapshot).
Abort the operation and pass the exception upward.

The author mentions that aborting can add much more complexity. For example, if a data structure has been partially initialized, then an exception occurs - “The exception handling code must restore consistency, such as by unwinding any changes made before the exception occurred.”

The author notes how easy and tempting it is to throw an exception and let the caller handle it. He argues that, as the developer of a certain method, if you are having trouble handling a certain exception, there’s a good chance the caller won’t know how to deal with it either.

“The best way to reduce the complexity damage caused by exception handling is to reduce the number of places where exceptions have to be handled.”

From here, the author shares a few techniques on how to reduce the number of exception handlers.

Define errors out of existence - “The best way to eliminate exception handling complexity is to define your APIs so that there are no exceptions to handle.” As an example, we can look at how file deletion is done on Windows compared to Linux. If you want to delete a file and it is open in another process, you will get an exception; you can’t perform the operation. In Linux, we can delete an open file - since we mark it for deletion at first.

Mask exceptions - “An exceptional condition is detected and handled at a low level in the system so that higher levels of software need not be aware of the condition.” For example, TCP masks packet loss by resending packets. So, higher-level software doesn’t need to know about the lost packets. It is guaranteed to have all packets.

Exception aggregation - “The idea behind exception aggregation is to handle many exceptions with a single piece of code; rather than writing distinct handlers for many individual exceptions, handle them all in one place with a single handler.”

Example
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49

	
public class FileProcessor
{
    public void ProcessFile(string filePath)
    {
        try
        {
            var config = ReadConfigFile(filePath);
            var processedData = ProcessData(config);
            WriteDataToFile(processedData, filePath);
        }
        catch (FileNotFoundException ex)
        {
            Console.WriteLine($"Config file not found: {ex.Message}");
            throw;
        }
        catch (IOException ex)
        {
            Console.WriteLine($"I/O error: {ex.Message}");
            throw new ApplicationException("I/O failure during file processing", ex);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Unexpected error: {ex.Message}");
            throw;
        }
    }

    private Config ReadConfigFile(string filePath)
    {
        if (!File.Exists(filePath))
        {
            throw new FileNotFoundException("The configuration file was not found.");
        }
        return new Config(filePath);
    }

    private void WriteDataToFile(ProcessedData data, string filePath)
    {
        try
        {
            File.WriteAllText(filePath, data.ToString());
        }
        catch (IOException ex)
        {
            Console.WriteLine("Failed to write file");
            throw;
        }
    }
}

Why is it bad?

Too Many Exception Handlers: There are multiple try-catch blocks in various parts of the code, which introduces duplication and complexity. Each method has its own error-handling logic, and exceptions are passed upwards without properly addressing the core issue.

Aborting Too Much: The ProcessFile method passes the responsibility of handling certain exceptions (like FileNotFoundException) back to the caller, increasing complexity. A caller may not know how to handle these errors, and passing them upwards creates more handlers across the system.

Fix 1: Define Errors Out of Existence

The first technique is to design the system to avoid exceptions altogether. Instead of throwing exceptions for things like missing files, we can redesign the ReadConfigFile method to treat the absence of a file as a normal condition, not an exceptional one.

1
2
3
4
5
6
7
8
9
10

	
private Config ReadConfigFile(string filePath)
{
    if (!File.Exists(filePath))
    {
        Console.WriteLine("Config file not found, using default settings.");
        return Config.GetDefaultConfig();  // Default behavior instead of exception
    }

    return new Config(filePath);
}

Why is it better?

No Exception Handling Needed: We avoid throwing FileNotFoundException entirely by defining the absence of a config file as an acceptable condition, with a default fallback.

Simplified Code: The caller doesn’t need to handle missing files—it simply gets a default configuration when no file is found.

Fix 2: Mask Exceptions

Next, we handle lower-level exceptions internally so that higher levels don’t need to worry about them. This is commonly used for network failures, file I/O, or similar situations where retrying or fallback mechanisms can mask the issue.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

	
private void WriteDataToFile(ProcessedData data, string filePath)
{
    // Mask exceptions: Retry writing the file instead of throwing an exception
    int retryCount = 3;
    while (retryCount > 0)
    {
        try
        {
            File.WriteAllText(filePath, data.ToString());
            break;
        }
        catch (IOException)
        {
            retryCount--;
            if (retryCount == 0)
            {
                Console.WriteLine("Failed to write after retries. Aborting.");
                // Depending on the system requirements, you might have to throw
                // an exception here as the issue was not transient,
                // or for example save the data to a tmp file, 
                // then try to write it to filePath at a later stage.
            }
        }
    }
}

Why is it better?
Retries with Masking: We attempt to retry the file write operation up to three times. This masks the IOException for transient errors (such as temporary file system issues), meaning higher-level code won’t need to worry about these exceptions.
Fix 3: Exception Aggregation

Instead of writing separate exception handlers for every possible error, we can aggregate exceptions and handle them in one place. This avoids duplicating exception handling logic.

Given that we still throw IOException, here’s how you might want to aggregate the exceptions.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

	
public void ProcessFile(string filePath)
{
    try
    {
        var config = ReadConfigFile(filePath);
        var processedData = ProcessData(config);
        WriteDataToFile(processedData, filePath);
    }
    catch (IOException ex) when (ex is FileNotFoundException || ex is UnauthorizedAccessException)
    {
        // Aggregated exception handler for all I/O-related exceptions
        Console.WriteLine($"I/O failure: {ex.Message}");
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Unexpected error: {ex.Message}");
        throw;
    }
}

Why is it better?

Aggregated Exceptions: We handle all IOException-related errors (such as file not found or access denied) in a single handler, avoiding duplicated error-handling logic.

Simpler Code: Instead of writing multiple catch blocks, we handle multiple related exceptions in one place, reducing the number of handlers.

Conclusion

A Philosophy of Software Design emphasizes that complexity is the silent killer of software systems, accumulating through seemingly small decisions.
The book describes the symptoms of complexity and how to treat them. In this blog post, I shared 3 ideas that resonated with me the most, but there are many more ideas in the book itself, so I definitely recommend reading it.

Note: I fed NotebookLLM the 33 page summary of the book, and it generated a 17 minutes long podcast that was pretty good honestly (above my expectations) - I shared it on the telegram channel.

Looking for a powerful, self-hosted backend for forms?
I’m building Collecto — a production-ready tool designed to handle your forms with ease and security. Check it out here and be part of its journey!

Copyright © 2022-2024 Eliran Turgeman
HomeAboutArchivesSearch
