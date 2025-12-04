package db

import (
	"gorm.io/gorm"
)

type Image struct {
	gorm.Model
	URL string
	Description string
}