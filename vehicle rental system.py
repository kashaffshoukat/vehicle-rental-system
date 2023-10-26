#include <iostream>
#include <vector>
#include <string>

class Vehicle {
public:
    Vehicle(std::string make, std::string model, int year)
        : make(make), model(model), year(year), rented(false) {}

    std::string getMake() const { return make; }
    std::string getModel() const { return model; }
    int getYear() const { return year; }
    bool isRented() const { return rented; }
    void rent() { rented = true; }
    void returnVehicle() { rented = false; }

private:
    std::string make;
    std::string model;
    int year;
    bool rented;
};

class RentalAgency {
public:
    void addVehicle(const Vehicle& vehicle) {
        vehicles.push_back(vehicle);
    }

    void rentVehicle(int index) {
        if (index >= 0 && index < vehicles.size() && !vehicles[index].isRented()) {
            vehicles[index].rent();
            std::cout << "Vehicle rented: " << vehicles[index].getMake() << " " << vehicles[index].getModel() << std::endl;
        } else {
            std::cout << "Invalid vehicle index or vehicle already rented." << std::endl;
        }
    }

    void returnVehicle(int index) {
        if (index >= 0 && index < vehicles.size() && vehicles[index].isRented()) {
            vehicles[index].returnVehicle();
            std::cout << "Vehicle returned: " << vehicles[index].getMake() << " " << vehicles[index].getModel() << std::endl;
        } else {
            std::cout << "Invalid vehicle index or vehicle not rented." << std::endl;
        }
    }

private:
    std::vector<Vehicle> vehicles;
};

int main() {
    RentalAgency rentalAgency;

    rentalAgency.addVehicle(Vehicle("Toyota", "Camry", 2022));
    rentalAgency.addVehicle(Vehicle("Honda", "Civic", 2021));
    rentalAgency.addVehicle(Vehicle("Ford", "Mustang", 2023));

    rentalAgency.rentVehicle(0);
    rentalAgency.rentVehicle(1);
    rentalAgency.returnVehicle(0);

    return 0;
}
