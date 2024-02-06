package com.reyesmicaela.programmingskillslevel3

/**
3. Real State Rent System

A real estate agency has 5 homes for rent. The homes are characterized by their size, number of bedrooms,
number of bathrooms, and location. The rental price of a home is calculated based on these factors.
Features:

First home: 200 square meters, 3 bedrooms, 2 bathrooms
Second home: 150 square meters, 2 bedrooms, 2 bathrooms
Third home: 100 square meters, 2 bedrooms, 1 bathroom
Fourth home: 100 square meters, 1 bedroom, 2 bathrooms
Fifth home: 80 square meters, 1 bedroom, 1 bathroom
The program must quote the price of the home according to: square meters, number of bedrooms, and number
of bathrooms. Each bedroom adds $40, and each bathroom adds $30. Each square meter has a cost of $90.
 */


fun main() {
    println("First home:")
    Home(200, 3, 2).calculate()
    println("Second home:")
    Home(150, 2, 2).calculate()
    println("Third home:")
    Home(100, 2, 1).calculate()
    println("Fourth home:")
    Home(100, 1, 2).calculate()
    println("Fifth home:")
    Home(80, 1, 1).calculate()
}

data class Home(
    val squareMeters: Int,
    val bedrooms: Int,
    val bathrooms: Int,
    val location: String? = null
) {
    val squareMetersCost = 90
    val bedroomsCost = 40
    val bathroomsCost = 30
}

fun Home.calculate() {
    println("$squareMeters square meters, $bedrooms bedrooms, $bathrooms bathrooms= $${squareMeters * squareMetersCost + bedrooms * bedroomsCost + bathrooms * bathroomsCost}")
}
