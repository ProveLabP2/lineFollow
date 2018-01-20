#ifndef __ANGLE_COMP_H__
#define __ANGLE_COMP_H__

#include <stdio.h>
#include <vector>
#include <Eigen/Dense>
using namespace Eigen;

const Vector2f NORMAL(0, 1);
float getAngleFirstLast(const std::vector<float> & lines);

#endif

