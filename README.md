A python library for running Monte-Carlo analyses

```python
import monte_carlo as mc

a = mc.Norm(interval=(5, 10)) # 90% confidence interval
b = mc.Norm(interval=(5, 10), proportion = 0.95) # 95% CI
c = mc.Norm(mean=0, sd=1)
print(c.s) # single sample

# Make a stackup function
def stackup():
    return a.s + b.s - (2 * c.s)

sim = mc.Simulation(f=stackup)
sim.run()

```
