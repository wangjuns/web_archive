# Numerically Stable Softmax and Cross Entropy | Jay Mody
December 15, 2022

* * *

In this post, we'll take a look at softmax and cross entropy loss, two very common mathematical functions used in deep learning. We'll see that naive implementations are numerically unstable, and then we'll derive implementations that are numerically stable.

Symbols
-------

* * *

*   : Input vector of dimensionality .
*   : Correct class, an integer on the range .
*   : Raw outputs (i.e. logits) of our neural network, vector of dimensionality .
*   We use to denote the natural logarithm.

Softmax
-------

* * *

The softmax function is defined as:  
  
The softmax function converts a vector of real numbers () to a vector of probabilities (such that and ). This is useful for converting the raw final output of a neural network (often referred to as **logits**) into probabilities.

In code:

```null
def softmax(x):
    
    return np.exp(x) / np.sum(np.exp(x))

x = np.array([1.2, 2, -4, 0.0]) 
softmax(x)


```

For very large inputs, we start seeing some numerical instability:

```null
x = np.array([1.2, 2000, -4000, 0.0])
softmax(x)


```

Why? Because floating point numbers aren't magic, they have limits:

```null
np.finfo(np.float64).max


np.finfo(np.float64).tiny


np.finfo(np.float64).smallest_subnormal


```

When we go beyond these limits, we start seeing funky behavior:

```null
np.finfo(np.float64).max * 2


np.inf - np.inf


np.finfo(np.float64).smallest_subnormal / 2


```

Looking back at our softmax example that resulted in `[0., nan, 0., 0.]`, we can see that the overflow of `np.exp(2000) = np.inf` is causing the `nan`, since we end up with `np.inf / np.inf = nan`.

If we want to avoid `nans`, we need to avoid `infs`.

To avoid `infs`, we need to avoid overflows.

To avoid overflows, we need to prevent our numbers from growing too large.

Underflows on the other hand don't seem quite as detrimental. Worst case scenario, we get the result `0` and lose all precision (i.e. `np.exp(-4000) = 0)`. While this is not ideal, this is a lot better than running into `inf` and `nan`.

Given the relative stability of floating point underflows vs overflows, how can we fix softmax?

Let's revisit our softmax equation and apply some tricks:  
  
Here, we're taking advantage of the rule . As a result, we are given the ability to offset our inputs by any constant of our choosing. For example, if we set that constant to :  

We get a numerically stable version of softmax:

*   All exponentiated values will be between 0 and 1 () since the value in the exponent is always negative ()
    *   This prevents overflow errors (but we are still prone to underflows)
*   At least one of the exponentiated values is 1 in the case when :
    *   i.e. at least one value is guaranteed not to underflow
    *   Thus, our denominator will always be , preventing division by zero errors
    *   We have at least one non-zero numerator, so softmax can't result in a zero vector

In code:

```null
def softmax(x):
    
    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))

x = np.array([1.2, 2, -4, 0])
softmax(x)



x = np.array([1.2, 2, -4, 0]) * 1000
softmax(x)


```

Cross Entropy and Log Softmax
-----------------------------

* * *

The cross entropy between two probability distributions is defined as.  
  
where and are our probability distributions represented as probability vectors (that is and are the probabilities of event occurring for and respectively). This [video has a great explanation for cross entropy](https://www.youtube.com/watch?v=ErfnhcEV1O8).

Roughly speaking, cross entropy measures the similarity of two probability distributions. In the context of neural networks, it's common to use cross entropy as a loss function for classification problems where:

*   is our predicted probabilities vector (i.e. the softmax of our raw network outputs, also called **logits**, denoted as ), that is
*   is a one-hot encoded vector of our label, that is a probability vector that assigns 100% probability to the position (our label for the correct class):

In this setup, cross entropy simplifies to:  

In code:

```null
def cross_entropy(y_hat, y_true):
    
    return -np.log(softmax(y_hat)[y_true])

cross_entropy(
    y_hat=np.random.normal(size=(10)),
    y_true=3,
)


```

For large numbers in `y_hat`, we start seeing `inf`:

```null
cross_entropy(
    y_hat = np.array([-1000, 1000]),
    y_true = 0,
)


```

The problem is that `softmax([-1000, 1000]) = [0, 1]`, and since `y_true = 0`, we get `-log(0) = inf`. So we need some way to avoid taking the log of zero. To prevent this, we can rearrange our equation for `log(softmax(x))`:  
  
This new equation guarantees that the sum inside the log will always be , so we no longer need to worry about `log(0)` errors.

In code:

```null
def log_softmax(x):
    
    x_max = np.max(x)
    return x - x_max - np.log(np.sum(np.exp(x - x_max)))

def cross_entropy(y_hat, y_true):
    return -log_softmax(y_hat)[y_true]

cross_entropy(
    y_hat=np.random.normal(size=(10)),
    y_true=3,
)



cross_entropy(
    y_hat = np.array([-1000, 1000]),
    y_true = 0,
)


```