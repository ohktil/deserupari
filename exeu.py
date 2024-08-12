class SomeClass:
    def __init__(self, value, other_value):
        self.value = value
        self.other_value = other_value

parent_instance = ParentClass()
instance = SomeClass(value=parent_instance.value, other_value=42)
