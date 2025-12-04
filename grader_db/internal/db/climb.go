package db

import (
	"gorm.io/gorm"
)

type Climb struct {
	gorm.Model
	Image 				Image
	GradeRealID			uint
	GradeGeneratedID	uint
	GradeReal 			Grades
	GradeGenerated 		Grades
}
