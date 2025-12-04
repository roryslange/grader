package db

import (
	"gorm.io/gorm"
)

type Climb_hold_xref struct {
	gorm.Model
	ID 			uint
	climb 		Climb
	hold 		Hold
	is_start 	bool
	is_end 		bool
}