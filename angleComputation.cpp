#include "angleComputation.hpp"
#include <iostream>


// Returns an angle of an array of lines using the first point and the last point
// in the lines. Angle is normalized between -1 (far left) and 1 (far right)
float getAngleFirstLast(const std::vector<float> & lines){
	if(lines.size() < 4){
		fprintf(stderr, "%s", "There are no lines in the passed in vector.\n"
						"A line consists of four floats (x1, y1, x2, y2)");
	}

	//assuming lines are already organized by y location
	const float firstPoint [2] = {lines[0], lines[1]};
	const float lastPoint [2] = {lines[lines.size() - 2],  lines[lines.size() - 1] };

	//line = x2 - x1, y2 - y1 where first point = x1, y1 and last point is x2, y2
	Vector2f line;
	line << lastPoint[0] - firstPoint[0], lastPoint[1] - firstPoint[1];
	line.normalize();
	float angle = line.dot(NORMAL);
	if(line[0] < 0){
		angle *= -1;
	}
	return angle;

}
