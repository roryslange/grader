package db

import (
	"gorm.io/gorm"
)

type Climb struct {
	gorm.Model
	ID 					uint
	image 				Image
	grade_real 			Grades
	grade_generated 	Grades
}
