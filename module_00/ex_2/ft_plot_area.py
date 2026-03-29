def ft_plot_area() -> None:
    """
    Prompts the user for a `lenght` and  `width`.
    And make `lenght` * `width`.
    """
    length: int = int(input("Enter length: "))
    width: int = int(input("Enter width: "))
    print(f"Plot area: {length * width}")
