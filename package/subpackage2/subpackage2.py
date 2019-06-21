if __name__ == "__main__":
    import package.package
    import package.subpackage1.subpackage1

print("subpackage2 __name__", __name__)
print("subpackage2 __package__", __package__)
