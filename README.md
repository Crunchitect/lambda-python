# Lambda python
Integrate [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus) into python

Make Functions:
```python
lambda_not = "Lx.x false true"
lambda_not_function = Lambda(lambda_not).to_function()
```

## Semantics
- Just as regular lambda calculus but instead of typing `λ`, you type `L`
- Constants like `FALSE` and `TRUE` are capitalized.

Examples:

> `λx.x` turns into `Lx.x`
>
> `λx.x FALSE TRUE` turns into `Lx.x FALSE TRUE`

### Why use lambda python?

Just out of pure boredom.