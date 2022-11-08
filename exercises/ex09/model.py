"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt

__author__ = "730575704"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, point_given) -> float:
        """Distance between 2 points."""
        x_distance: float = (self.x - point_given.x) ** 2
        y_distance: float = (self.y - point_given.y) ** 2
        return sqrt(x_distance + y_distance)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Update cell with tick."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        vulnerable = self.is_vulnerable()
        infected = self.is_infected()
        immune = self.is_immune()
        if vulnerable:
            return "gray"
        elif infected:
            return "green"
        elif immune:
            return "blue"
        return "black"

    def contract_disease(self) -> None:
        """Cell contracts disease."""
        self.sickness = constants.INFECTED

    def immunize(self) -> None:
        """Cell immunized."""
        self.sickness = constants.IMMUNE

    def is_vulnerable(self) -> bool:
        """Checks if cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        return False

    def is_infected(self) -> bool:
        """Checks if cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        return False

    def is_immune(self) -> bool:
        """Checks if cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        return False

    def contact_with(self, other_cell) -> None:
        """Contact with other cell infection spread."""
        if self.is_infected() and other_cell.is_vulnerable():
            other_cell.contract_disease()

        if other_cell.is_infected() and self.is_vulnerable():
            self.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, starting_infected: int, starting_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []

        if starting_infected + starting_immune >= cells:
            raise ValueError("Please have less immune and infected cells than the total cell count.")

        if starting_infected >= cells or starting_infected <= 0:
            raise ValueError("Must start with some infected cells.")

        if starting_immune >= cells or starting_immune < 0:
            raise ValueError("Please enter a valid immune cell count.")

        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)

        for cell_object in range(starting_infected):
            self.population[cell_object].contract_disease()

        inverse_index: int = -1

        while abs(inverse_index) <= starting_immune:
            self.population[inverse_index].immunize()
            inverse_index -= 1
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)
    
    def check_contacts(self) -> None:
        """Checks if cells contact each other."""
        i = 0
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                distance_between: float = self.population[i].location.distance(self.population[j].location)
                if distance_between < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1
            i += 1

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell_test in self.population:
            if cell_test.is_infected():
                return False
        return True