package db

import (
	"gorm.io/gorm"
)

type Grades struct {
	gorm.Model
	ID 		uint
	grade 	string
}