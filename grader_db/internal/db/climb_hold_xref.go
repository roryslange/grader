package db

import (
	"gorm.io/gorm"
)

type Climb_hold_xref struct {
	gorm.Model
	ClimbID		uint
	HoldID		uint
	Climb 		Climb
	Hold		Hold
	IsStart 	bool
	IsEnd		bool
}