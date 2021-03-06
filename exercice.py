import math

def square_root(a: float) -> float:
    return math.sqrt(a)



def square(a: float) -> float:
    Result_sqrt = a*a
    return Result_sqrt


def average(a: float, b: float, c: float) -> float:
    Result_avrg = (a + b + c)/3
    return Result_avrg


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    Full_degree = angle_degs + angle_mins/60 + angle_secs/3600
    Radians_Result = (Full_degree*math.pi)/180
    return Radians_Result


def to_degrees(angle_rads: float) -> tuple:
    Degré_complet = angle_rads *180/math.pi
    Approx = (Degré_complet-int(Degré_complet))*60
    Degré, Minutes, Secondes = int(Degré_complet), int(Approx), (Approx-int(Approx))*60
    return Degré, Minutes, Secondes


def to_celsius(temperature: float) -> float:
    return (temperature-32)/1.8


def to_farenheit(temperature: float) -> float:
    return temperature*1.8 +32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()

