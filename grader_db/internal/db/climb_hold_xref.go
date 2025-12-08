package db

import (
	"gorm.io/gorm"
)

type Climb_hold_xref struct {
	gorm.Model
	ClimbID		uint
	HoldID		uint
	IsStart 	bool
	IsEnd		bool
	Climb 		Climb
	Hold		Hold
}