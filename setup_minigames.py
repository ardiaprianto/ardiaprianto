import os

def create_files():
    # 1. Update HTML files
    files = [
        "index.html",
        "profile.html",
        "informatika.html",
        "bahasa-indonesia.html",
        "schedule.html"
    ]
    
    desktop_link = """                    <a href="minigames.html" id="nav-minigames"
                        class="nav-btn px-4 py-2 rounded-md font-medium text-sm transition-all duration-200">
                        <i class="fa-solid fa-gamepad mr-1.5 text-xs opacity-75"></i> Mini Games
                    </a>
"""
    
    mobile_link = """            <a href="minigames.html" id="mobile-nav-minigames"
                class="mobile-nav-btn w-full text-left px-4 py-3 rounded-lg text-base font-medium flex items-center justify-between">
                <span><i class="fa-solid fa-gamepad mr-3"></i> Mini Games</span>
                <i class="fa-solid fa-chevron-right text-xs opacity-50"></i>
            </a>
"""
    
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        updated = False
        if 'id="nav-minigames"' not in content:
            content = content.replace("                </nav>", desktop_link + "                </nav>")
            content = content.replace("        </div>\n    </header>", mobile_link + "        </div>\n    </header>")
            # Fix issue if profile.html has extra newline
            content = content.replace("            </a>\n        </div>\n    </header>", "            </a>\n" + mobile_link + "        </div>\n    </header>")
            updated = True
            
        if updated:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
                print(f"Updated {f}")
    
    # 2. Create minigames.html
    with open('index.html', 'r', encoding='utf-8') as file:
        index_content = file.read()
        
    index_content = index_content.replace('id="nav-dashboard"\n                        class="nav-btn active-nav', 'id="nav-dashboard"\n                        class="nav-btn')
    index_content = index_content.replace('id="nav-minigames"\n                        class="nav-btn', 'id="nav-minigames"\n                        class="nav-btn active-nav')
    index_content = index_content.replace('id="mobile-nav-dashboard"\n                class="mobile-nav-btn active-mobile-nav', 'id="mobile-nav-dashboard"\n                class="mobile-nav-btn')
    index_content = index_content.replace('id="mobile-nav-minigames"\n                class="mobile-nav-btn', 'id="mobile-nav-minigames"\n                class="mobile-nav-btn active-mobile-nav')
    
    main_start = index_content.find('<main')
    main_end = index_content.find('</main>') + 7
    
    header = index_content[:main_start]
    footer = index_content[main_end:]
    
    footer = footer.replace('<script src="assets/js/main.js"></script>', '<script src="assets/js/main.js"></script>\n    <script src="assets/js/minigames.js"></script>\n    <script src="assets/js/xox.js"></script>\n    <script src="assets/js/snake.js"></script>')
    
    # Check title
    header = header.replace('<title>Dashboard | Ardi Aprianto (Ardi.a) | Portfolio & Digital Space</title>', '<title>Mini Games | Ardi Aprianto (Ardi.a) | Portfolio & Digital Space</title>')
    
    minigames_main = """<main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
        <section id="sec-minigames" class="tab-content w-full">
            <div class="text-center mb-12">
                <h1 class="font-serif text-3xl sm:text-4xl md:text-5xl font-bold text-om-navy dark:text-om-gold mb-4">
                    Mini Games
                </h1>
                <p class="text-base md:text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
                    Mainkan game sederhana dan seru langsung di website
                </p>
            </div>

            <!-- Game Selection Cards -->
            <div id="game-selection" class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                <!-- XOX Card -->
                <div class="group relative overflow-hidden rounded-2xl bg-om-card-light dark:bg-om-card-dark border border-om-gold/30 p-8 shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-20 h-20 rounded-full bg-om-navy/10 dark:bg-om-gold/10 text-om-navy dark:text-om-gold flex items-center justify-center text-4xl mb-6 group-hover:scale-110 transition-transform">
                        <i class="fa-solid fa-xmarks-lines"></i>
                    </div>
                    <h3 class="font-serif text-2xl font-bold text-om-navy dark:text-white mb-3">XOX</h3>
                    <p class="text-gray-600 dark:text-gray-400 mb-8 flex-grow">
                        Tantang temanmu dalam permainan Tic-Tac-Toe
                    </p>
                    <button onclick="showGame('xox')" class="px-8 py-3 rounded-lg bg-om-navy text-om-cream dark:bg-om-gold dark:text-om-navy font-semibold text-sm hover:opacity-90 transition-all duration-200 shadow-md w-full">
                        Mainkan XOX
                    </button>
                </div>

                <!-- Snake Card -->
                <div class="group relative overflow-hidden rounded-2xl bg-om-card-light dark:bg-om-card-dark border border-om-gold/30 p-8 shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-20 h-20 rounded-full bg-om-navy/10 dark:bg-om-gold/10 text-om-emerald dark:text-om-emerald flex items-center justify-center text-4xl mb-6 group-hover:scale-110 transition-transform">
                        <i class="fa-solid fa-staff-snake"></i>
                    </div>
                    <h3 class="font-serif text-2xl font-bold text-om-navy dark:text-white mb-3">Snake Game</h3>
                    <p class="text-gray-600 dark:text-gray-400 mb-8 flex-grow">
                        Kendalikan ular, makan makanan, dan raih skor tertinggi
                    </p>
                    <button onclick="showGame('snake')" class="px-8 py-3 rounded-lg bg-om-navy text-om-cream dark:bg-om-gold dark:text-om-navy font-semibold text-sm hover:opacity-90 transition-all duration-200 shadow-md w-full">
                        Mainkan Snake
                    </button>
                </div>
            </div>

            <!-- XOX Game Area -->
            <div id="game-xox" class="hidden max-w-lg mx-auto bg-om-card-light dark:bg-om-card-dark border border-om-gold/30 rounded-2xl p-6 md:p-8 shadow-xl">
                <div class="flex justify-between items-center mb-6">
                    <h2 class="font-serif text-2xl font-bold text-om-navy dark:text-om-gold">XOX (Tic-Tac-Toe)</h2>
                    <button onclick="showGameSelection()" class="text-sm px-4 py-2 rounded border border-om-gold text-om-navy dark:text-om-gold hover:bg-om-gold/10 transition-all">Kembali</button>
                </div>
                <!-- Scores -->
                <div class="flex justify-between mb-6 text-center">
                    <div class="bg-om-cream-dark dark:bg-om-navy px-4 py-2 rounded-lg flex-1 mx-1 border border-om-gold/20 shadow-sm">
                        <div class="text-xs text-gray-500 font-bold uppercase">Skor X</div>
                        <div id="score-x" class="text-xl font-bold text-om-navy dark:text-white">0</div>
                    </div>
                    <div class="bg-om-cream-dark dark:bg-om-navy px-4 py-2 rounded-lg flex-1 mx-1 border border-om-gold/20 shadow-sm">
                        <div class="text-xs text-gray-500 font-bold uppercase">Seri</div>
                        <div id="score-tie" class="text-xl font-bold text-gray-500">0</div>
                    </div>
                    <div class="bg-om-cream-dark dark:bg-om-navy px-4 py-2 rounded-lg flex-1 mx-1 border border-om-gold/20 shadow-sm">
                        <div class="text-xs text-gray-500 font-bold uppercase">Skor O</div>
                        <div id="score-o" class="text-xl font-bold text-om-navy dark:text-white">0</div>
                    </div>
                </div>
                <!-- Status -->
                <div id="xox-status" class="text-center font-bold text-lg mb-6 text-om-navy dark:text-om-gold">Giliran: X</div>
                <!-- Board -->
                <div class="grid grid-cols-3 gap-3 mb-6" id="xox-board">
                    <!-- JS injects cells -->
                </div>
                <!-- Controls -->
                <div class="flex gap-4">
                    <button id="btn-xox-restart" class="flex-1 px-4 py-3 rounded-lg bg-om-navy text-om-cream dark:bg-om-gold dark:text-om-navy font-semibold hover:opacity-90 transition-all shadow-md">Main Lagi</button>
                    <button id="btn-xox-reset-score" class="flex-1 px-4 py-3 rounded-lg border border-red-500 text-red-500 hover:bg-red-500/10 font-semibold transition-all shadow-sm">Reset Skor</button>
                </div>
            </div>

            <!-- Snake Game Area -->
            <div id="game-snake" class="hidden max-w-xl mx-auto bg-om-card-light dark:bg-om-card-dark border border-om-gold/30 rounded-2xl p-6 md:p-8 shadow-xl">
                <div class="flex justify-between items-center mb-6">
                    <h2 class="font-serif text-2xl font-bold text-om-navy dark:text-om-gold">Snake Game</h2>
                    <button onclick="showGameSelection()" class="text-sm px-4 py-2 rounded border border-om-gold text-om-navy dark:text-om-gold hover:bg-om-gold/10 transition-all">Kembali</button>
                </div>
                <!-- Scores -->
                <div class="flex justify-between mb-6 text-center">
                    <div class="bg-om-cream-dark dark:bg-om-navy px-6 py-2 rounded-lg border border-om-gold/20 shadow-sm">
                        <div class="text-xs text-gray-500 font-bold uppercase">Score</div>
                        <div id="snake-score" class="text-xl font-bold text-om-navy dark:text-white">0</div>
                    </div>
                    <div class="bg-om-cream-dark dark:bg-om-navy px-6 py-2 rounded-lg border border-om-gold/20 shadow-sm">
                        <div class="text-xs text-gray-500 font-bold uppercase">High Score</div>
                        <div id="snake-highscore" class="text-xl font-bold text-om-gold">0</div>
                    </div>
                </div>
                <!-- Game Canvas Container -->
                <div class="relative bg-black rounded-lg overflow-hidden flex justify-center items-center shadow-inner mb-6 mx-auto w-full max-w-[400px]" style="aspect-ratio: 1/1;">
                    <canvas id="snake-canvas" width="400" height="400" class="block w-full h-full object-contain"></canvas>
                    <div id="snake-overlay" class="absolute inset-0 bg-black/80 flex flex-col items-center justify-center pointer-events-none transition-opacity duration-300">
                        <div id="snake-gameover-text" class="text-red-500 font-bold text-3xl mb-4 hidden">GAME OVER</div>
                        <button id="btn-snake-start" class="px-6 py-3 rounded-lg bg-om-gold text-om-navy font-bold hover:scale-105 transition-transform pointer-events-auto shadow-lg">Mulai Game</button>
                    </div>
                </div>
                
                <!-- Mobile Controls -->
                <div class="grid grid-cols-3 gap-2 max-w-[180px] mx-auto md:hidden mb-6">
                    <div></div>
                    <button id="btn-snake-up" class="w-14 h-14 bg-om-cream-dark dark:bg-om-navy rounded-lg shadow border border-om-gold/20 flex items-center justify-center text-2xl active:scale-95 transition-transform text-om-navy dark:text-om-gold"><i class="fa-solid fa-arrow-up"></i></button>
                    <div></div>
                    <button id="btn-snake-left" class="w-14 h-14 bg-om-cream-dark dark:bg-om-navy rounded-lg shadow border border-om-gold/20 flex items-center justify-center text-2xl active:scale-95 transition-transform text-om-navy dark:text-om-gold"><i class="fa-solid fa-arrow-left"></i></button>
                    <button id="btn-snake-down" class="w-14 h-14 bg-om-cream-dark dark:bg-om-navy rounded-lg shadow border border-om-gold/20 flex items-center justify-center text-2xl active:scale-95 transition-transform text-om-navy dark:text-om-gold"><i class="fa-solid fa-arrow-down"></i></button>
                    <button id="btn-snake-right" class="w-14 h-14 bg-om-cream-dark dark:bg-om-navy rounded-lg shadow border border-om-gold/20 flex items-center justify-center text-2xl active:scale-95 transition-transform text-om-navy dark:text-om-gold"><i class="fa-solid fa-arrow-right"></i></button>
                </div>
                
                <p class="text-center text-xs text-gray-500 hidden md:block">Gunakan Arrow Keys (↑ ↓ ← →) untuk bergerak.</p>
            </div>
            
            <style>
                .xox-cell {
                    width: 100%;
                    aspect-ratio: 1/1;
                    border: 2px solid rgba(197, 160, 89, 0.3);
                    border-radius: 0.5rem;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 3.5rem;
                    font-weight: bold;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }
                .xox-cell:hover {
                    background-color: rgba(197, 160, 89, 0.1);
                }
                .xox-cell.x-mark {
                    color: #0E1B2E; /* om-navy */
                }
                html.dark .xox-cell.x-mark {
                    color: #FFFFFF;
                }
                .xox-cell.o-mark {
                    color: #C5A059; /* om-gold */
                }
                .xox-win-highlight {
                    background-color: rgba(197, 160, 89, 0.3) !important;
                    box-shadow: inset 0 0 15px rgba(197, 160, 89, 0.5);
                    transform: scale(1.05);
                    z-index: 10;
                    border-color: rgba(197, 160, 89, 1);
                }
            </style>
        </section>
    </main>"""

    with open('minigames.html', 'w', encoding='utf-8') as file:
        file.write(header + minigames_main + footer)
    print("Created minigames.html")
    
    # 3. Create JS files
    minigames_js = """// Minigames Page Logic
function showGameSelection() {
    document.getElementById('game-selection').classList.remove('hidden');
    document.getElementById('game-xox').classList.add('hidden');
    document.getElementById('game-snake').classList.add('hidden');
    
    // Trigger stop game logic if needed
    if (window.stopSnakeGame) {
        window.stopSnakeGame();
    }
}

function showGame(game) {
    document.getElementById('game-selection').classList.add('hidden');
    
    if (game === 'xox') {
        document.getElementById('game-xox').classList.remove('hidden');
        if (window.initXOX) window.initXOX();
    } else if (game === 'snake') {
        document.getElementById('game-snake').classList.remove('hidden');
        if (window.initSnake) window.initSnake();
    }
}
"""
    with open('assets/js/minigames.js', 'w', encoding='utf-8') as f:
        f.write(minigames_js)
    
    xox_js = """// XOX (Tic-Tac-Toe) Logic
(function() {
    let board = ['', '', '', '', '', '', '', '', ''];
    let currentPlayer = 'X';
    let gameActive = false;
    
    let scores = { X: 0, O: 0, Tie: 0 };
    
    const winConditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Cols
        [0, 4, 8], [2, 4, 6]             // Diagonals
    ];

    function renderBoard() {
        const boardEl = document.getElementById('xox-board');
        boardEl.innerHTML = '';
        board.forEach((cell, index) => {
            const cellEl = document.createElement('div');
            cellEl.classList.add('xox-cell');
            if (cell === 'X') cellEl.classList.add('x-mark');
            if (cell === 'O') cellEl.classList.add('o-mark');
            cellEl.innerText = cell;
            cellEl.addEventListener('click', () => handleCellClick(index, cellEl));
            cellEl.setAttribute('data-index', index);
            boardEl.appendChild(cellEl);
        });
    }
    
    function handleCellClick(index, cellEl) {
        if (board[index] !== '' || !gameActive) return;
        
        board[index] = currentPlayer;
        cellEl.innerText = currentPlayer;
        if (currentPlayer === 'X') cellEl.classList.add('x-mark');
        else cellEl.classList.add('o-mark');
        
        checkWin();
    }
    
    function checkWin() {
        let roundWon = false;
        let winLine = [];
        
        for (let i = 0; i < winConditions.length; i++) {
            const [a, b, c] = winConditions[i];
            if (board[a] && board[a] === board[b] && board[a] === board[c]) {
                roundWon = true;
                winLine = [a, b, c];
                break;
            }
        }
        
        if (roundWon) {
            document.getElementById('xox-status').innerText = currentPlayer + ' Menang!';
            scores[currentPlayer]++;
            updateScores();
            gameActive = false;
            highlightWin(winLine);
            return;
        }
        
        if (!board.includes('')) {
            document.getElementById('xox-status').innerText = 'Seri!';
            scores.Tie++;
            updateScores();
            gameActive = false;
            return;
        }
        
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        document.getElementById('xox-status').innerText = 'Giliran: ' + currentPlayer;
    }
    
    function highlightWin(winLine) {
        const cells = document.querySelectorAll('.xox-cell');
        winLine.forEach(index => {
            cells[index].classList.add('xox-win-highlight');
        });
    }
    
    function updateScores() {
        document.getElementById('score-x').innerText = scores.X;
        document.getElementById('score-o').innerText = scores.O;
        document.getElementById('score-tie').innerText = scores.Tie;
    }
    
    function restartGame() {
        board = ['', '', '', '', '', '', '', '', ''];
        currentPlayer = 'X';
        gameActive = true;
        document.getElementById('xox-status').innerText = 'Giliran: ' + currentPlayer;
        renderBoard();
    }
    
    function resetScore() {
        scores = { X: 0, O: 0, Tie: 0 };
        updateScores();
        restartGame();
    }
    
    window.initXOX = function() {
        if (!document.getElementById('xox-board')) return;
        restartGame();
        
        const restartBtn = document.getElementById('btn-xox-restart');
        const resetScoreBtn = document.getElementById('btn-xox-reset-score');
        
        // Remove existing listeners by cloning
        const newRestart = restartBtn.cloneNode(true);
        restartBtn.parentNode.replaceChild(newRestart, restartBtn);
        newRestart.addEventListener('click', restartGame);
        
        const newReset = resetScoreBtn.cloneNode(true);
        resetScoreBtn.parentNode.replaceChild(newReset, resetScoreBtn);
        newReset.addEventListener('click', resetScore);
    };

})();
"""
    with open('assets/js/xox.js', 'w', encoding='utf-8') as f:
        f.write(xox_js)
    
    snake_js = """// Snake Game Logic
(function() {
    const canvas = document.getElementById('snake-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    const gridSize = 20;
    const tileCount = canvas.width / gridSize; // 400 / 20 = 20
    
    let snake = [];
    let food = {};
    let dx = 0;
    let dy = 0;
    let score = 0;
    let highScore = localStorage.getItem('snakeHighScore') || 0;
    
    let gameLoopTimeout;
    let isGameOver = false;
    let gameStarted = false;
    let speed = 120;
    
    // Initialize UI
    document.getElementById('snake-highscore').innerText = highScore;
    
    function resetGame() {
        snake = [
            { x: 10, y: 10 },
            { x: 9, y: 10 },
            { x: 8, y: 10 }
        ];
        dx = 1;
        dy = 0;
        score = 0;
        speed = 120;
        isGameOver = false;
        document.getElementById('snake-score').innerText = score;
        spawnFood();
        
        document.getElementById('snake-overlay').classList.add('opacity-0');
        document.getElementById('snake-overlay').classList.add('pointer-events-none');
        document.getElementById('snake-gameover-text').classList.add('hidden');
        document.getElementById('btn-snake-start').innerText = "Main Lagi";
        
        clearTimeout(gameLoopTimeout);
        gameStarted = true;
        gameLoop();
    }
    
    function spawnFood() {
        food = {
            x: Math.floor(Math.random() * tileCount),
            y: Math.floor(Math.random() * tileCount)
        };
        // Ensure food doesn't spawn on snake
        for (let segment of snake) {
            if (segment.x === food.x && segment.y === food.y) {
                spawnFood();
                break;
            }
        }
    }
    
    function gameLoop() {
        if (!gameStarted || isGameOver) return;
        
        update();
        draw();
        
        if (!isGameOver) {
            gameLoopTimeout = setTimeout(gameLoop, speed);
        }
    }
    
    function update() {
        const head = { x: snake[0].x + dx, y: snake[0].y + dy };
        
        // Wall collision
        if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
            gameOver();
            return;
        }
        
        // Self collision
        for (let i = 0; i < snake.length; i++) {
            if (head.x === snake[i].x && head.y === snake[i].y) {
                gameOver();
                return;
            }
        }
        
        snake.unshift(head);
        
        // Food collision
        if (head.x === food.x && head.y === food.y) {
            score += 10;
            document.getElementById('snake-score').innerText = score;
            
            if (score > highScore) {
                highScore = score;
                localStorage.setItem('snakeHighScore', highScore);
                document.getElementById('snake-highscore').innerText = highScore;
            }
            
            // Increase speed slightly
            if (speed > 50) speed -= 2;
            
            spawnFood();
        } else {
            snake.pop();
        }
    }
    
    function draw() {
        // Clear canvas
        ctx.fillStyle = '#1A1A1A';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Draw food
        ctx.fillStyle = '#ef4444'; // Red
        ctx.beginPath();
        ctx.arc(food.x * gridSize + gridSize/2, food.y * gridSize + gridSize/2, gridSize/2 - 2, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw snake
        snake.forEach((segment, index) => {
            ctx.fillStyle = index === 0 ? '#10b981' : '#34d399'; // Emerald green
            // Slightly smaller than grid size to show gaps between segments
            ctx.fillRect(segment.x * gridSize + 1, segment.y * gridSize + 1, gridSize - 2, gridSize - 2);
        });
    }
    
    function gameOver() {
        isGameOver = true;
        gameStarted = false;
        document.getElementById('snake-overlay').classList.remove('opacity-0');
        document.getElementById('snake-overlay').classList.remove('pointer-events-none');
        document.getElementById('snake-gameover-text').classList.remove('hidden');
    }
    
    // Keyboard controls
    document.addEventListener('keydown', (e) => {
        if (!gameStarted) return;
        switch (e.key) {
            case 'ArrowUp':
                if (dy !== 1) { dx = 0; dy = -1; e.preventDefault(); }
                break;
            case 'ArrowDown':
                if (dy !== -1) { dx = 0; dy = 1; e.preventDefault(); }
                break;
            case 'ArrowLeft':
                if (dx !== 1) { dx = -1; dy = 0; e.preventDefault(); }
                break;
            case 'ArrowRight':
                if (dx !== -1) { dx = 1; dy = 0; e.preventDefault(); }
                break;
        }
    });
    
    // Mobile controls
    document.getElementById('btn-snake-up')?.addEventListener('click', () => { if (dy !== 1) { dx = 0; dy = -1; } });
    document.getElementById('btn-snake-down')?.addEventListener('click', () => { if (dy !== -1) { dx = 0; dy = 1; } });
    document.getElementById('btn-snake-left')?.addEventListener('click', () => { if (dx !== 1) { dx = -1; dy = 0; } });
    document.getElementById('btn-snake-right')?.addEventListener('click', () => { if (dx !== -1) { dx = 1; dy = 0; } });
    
    const startBtn = document.getElementById('btn-snake-start');
    if(startBtn) {
        // use cloning to prevent duplicate listeners
        const newStart = startBtn.cloneNode(true);
        startBtn.parentNode.replaceChild(newStart, startBtn);
        newStart.addEventListener('click', resetGame);
    }
    
    window.initSnake = function() {
        // Initial draw before start
        document.getElementById('snake-overlay').classList.remove('opacity-0');
        document.getElementById('snake-overlay').classList.remove('pointer-events-none');
        document.getElementById('snake-gameover-text').classList.add('hidden');
        document.getElementById('btn-snake-start').innerText = "Mulai Game";
        
        ctx.fillStyle = '#1A1A1A';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        gameStarted = false;
        isGameOver = false;
        clearTimeout(gameLoopTimeout);
    };
    
    window.stopSnakeGame = function() {
        gameStarted = false;
        isGameOver = true;
        clearTimeout(gameLoopTimeout);
    };

})();
"""
    with open('assets/js/snake.js', 'w', encoding='utf-8') as f:
        f.write(snake_js)

create_files()
