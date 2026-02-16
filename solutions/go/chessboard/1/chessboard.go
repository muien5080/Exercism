package chessboard

// File represents a vertical file (A–H) containing 8 ranks.
type File []bool

// Chessboard maps file names ("A"–"H") to Files.
type Chessboard map[string]File

// CountInFile returns how many squares are occupied in the chessboard,
// within the given file.
func CountInFile(board Chessboard, file string) int {
	count := 0

	for f, ranks := range board {
		if f == file {
			for _, occupied := range ranks {
				if occupied {
					count++
				}
			}
		}
	}

	return count
}

// CountInRank returns how many squares are occupied in the chessboard,
// within the given rank.
func CountInRank(board Chessboard, rank int) int {
	if rank < 1 || rank > 8 {
		return 0
	}

	count := 0

	for _, ranks := range board {
		// rank-1 because slice index starts at 0
		if ranks[rank-1] {
			count++
		}
	}

	return count
}

// CountAll should count how many squares are present in the chessboard.
func CountAll(cb Chessboard) int {
	count := 0

	for _, file := range cb {
		for range file {
			count++
		}
	}

	return count
}

// CountOccupied returns how many squares are occupied in the chessboard.
func CountOccupied(cb Chessboard) int {
	count := 0

	for _, file := range cb {
		for _, occupied := range file {
			if occupied {
				count++
			}
		}
	}

	return count
}
