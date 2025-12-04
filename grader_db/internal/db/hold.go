package db

import (
	"gorm.io/gorm"
)

type Hold struct {
	gorm.Model
	ID			uint
	color 		string
	hold_type 	string
}