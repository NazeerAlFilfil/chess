# Chess Game - Python (Pygame & PyOpenGL)

## Overview
This is a Chess game implemented in Python using **Pygame** for the graphical interface and **PyOpenGL** for rendering the game board and pieces. The game currently supports all the standard chess rules, including piece movement, capturing, and castling. However, the logic for detecting game-ending conditions (checkmate, stalemate) is still a work in progress.

## Features
- Fully functional chessboard with an interactive graphical interface.
- Support for all standard chess rules:
  - Piece-specific movements (pawns, knights, bishops, rooks, queens, and kings).
  - Capturing opponent pieces.
  - Castling (both kingside and queenside).
  - En passant capture.
  - Pawn promotion.
- Visual representation of moves and captures.
- Turn-based gameplay between two players.
- Highlighting valid moves for a selected piece.

## Missing Features
- **Game-ending conditions:**
  - Detection of checkmate.
  - Detection of stalemate.
  - Draw conditions (e.g., insufficient material, threefold repetition).
- **AI/Computer Opponent:** Currently, the game only supports two-player gameplay on the same device.

## Getting Started
### Prerequisites
- Python 3.x
- Pygame
- PyOpenGL
- PyOpenGL_accelerate

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd chess
   ```
2. Install the required dependencies:
   ```bash
   pip install pygame PyOpenGL PyOpenGL_accelerate
   ```
3. Run the game:
   ```bash
   python main.py
   ```

### Controls
- **Left Mouse Button:** Select and move pieces.

## How It Works
- The chessboard and pieces are rendered using PyOpenGL.
- User interactions are handled via Pygame events.
- The game logic ensures that each piece follows its specific movement rules.
- Turn management alternates between the white and black players.

## Known Issues
- Game does not currently detect check, checkmate, or stalemate.
- No undo/redo functionality.

## Contributing
Contributions are welcome! If you have ideas or want to fix bugs, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

