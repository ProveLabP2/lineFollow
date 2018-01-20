#include "angleComputation.hpp"
#include <vector>

int main(int argc, char ** args){
	const std::vector<float> testLines = {50, 10, 5, 100}; 	//should point left
	const std::vector<float> testLines2 = {50, 10, 100, 100}; //should point right
	
	float angle = getAngleFirstLast(testLines);
	printf("angle: %f\n", angle);
	angle = getAngleFirstLast(testLines2);
	printf("angle: %f\n", angle);
}