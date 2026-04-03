#! /usr/bin/python3

def get_player_pos() -> tuple:
    """
    Prompt user for coordinates

    Returns:
        tuple: x, y and z coordinates
    """
    # coordinates 
    while True:
        try:
            usr_input: str = input("Enter new coordinates as floats in format `x, y, z`: ")
            lst_input = usr_input.split(",")
            assert len(lst_input) == 3  # Check is there is only 3 arguments
            coordinates = tuple([float(x) for x in lst_input])
            print(coordinates)
            return coordinates

        except Exception as e:
            print("error, try again")


def main() -> None:
    """
    Main function
    """
    get_player_pos()
    

if __name__ == "__main__":
    main()