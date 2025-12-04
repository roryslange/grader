package db

import (
	"gorm.io/gorm"
)

type Image struct {
	gorm.Model
	ID 	uint
	url string
}