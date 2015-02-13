def reverse(name):
    return reduce(lambda a, b: b + a, name)

print reverse("Jamin")
