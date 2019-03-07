A python library for running Monte-Carlo analyses

```python
import monte_carlo as mc

# Random variable given 90% confidence interval (default)
a = mc.Norm(interval=(5, 10))

# Random variable given 95% confidence interval (default)
b = mc.Norm(interval=(5, 10), proportion = 0.95)

# Specify mean and standard deviation
c = mc.Norm(mean=0, sd=1)

# Get a sample
c.sample()
```
