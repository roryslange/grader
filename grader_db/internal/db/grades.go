package db

import (
	"gorm.io/gorm"
)

type Grades struct {
	gorm.Model
	Grade 	string
}