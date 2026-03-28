import jax.numpy as jnp

u = jnp.array([6,1])
v = jnp.array([2,3])
c = 2

lhs = c * (u + v)
rhs = (c*u) + (c*v)
print(f"LHS: {lhs}")
print(f"RHS: {rhs}")