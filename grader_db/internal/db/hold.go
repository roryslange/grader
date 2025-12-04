package db

import (
	"gorm.io/gorm"
)

type Hold struct {
	gorm.Model
	Color 		string
	HoldType 	string
}