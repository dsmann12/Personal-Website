class Position {
    constructor(x = 0, y = 0) {
        this.x = x;
        this.y = y;
    }
}

class Velocity {
    constructor(dx = 0, dy = 0) {
        this.dx = dx;
        this.dy = dy;
    }
}

class Shape {
    constructor(x = 0, y = 0) {
        this.pos = new Position(x, y);
        this.vel = new Velocity(0, 0);
    }
}

class Ball extends Shape {
    constructor(x = 0, y = 0, radius = 10) {
        super(x, y);
        this.vel.dx = 10;
        this.vel.dy = 10;
        this.radius = radius;
    }

    // Get positions
    get top() {
        return this.pos.y - this.radius;
    }

    get right() {
        return this.pos.x + this.radius;
    }

    get bottom() {
        return this.pos.y + this.radius;
    }

    get left() {
        return this.pos.x - this.radius;
    }

    collide() {

    }

    reset() {
        let x = 70;
        let y = 20;
        let dx = 10;
        let dy = Math.abs((Math.random() > 0.5) ? (ball.vel.dy * 0.5) : (ball.vel.dy * 0.25));
        if (ball.right < 0) {
            x = canvas.width - 40;
            dx = -dx;
        }
    
        ball.pos.x = x;
        ball.pos.y = y;
        ball.vel.dx = dx;
        ball.vel.dy = dy;
    }

    draw() {
        context.fillStyle = 'white';
        context.beginPath();
        context.arc(this.pos.x, this.pos.y, this.radius, 0, Math.PI*2, true);
        context.fill();
    }

    update() {
       this.pos.x += this.vel.dx;
       this.pos.y += this.vel.dy;
    }
}

class Player extends Shape {
    constructor(x = 0, y = 0, height = 100, width = 25) {
        super(x, y);
        this.vel.dy = 10;
        this.height = height;
        this.width = width;
        this.oldY = this.pos.y;
        this.score = 0;
    }

    // Get positions
    get top() {
        return this.pos.y;
    }

    get right() {
        return this.pos.x + this.width;
    }

    get bottom() {
        return this.pos.y + this.height;
    }

    get left() {
        return this.pos.x;
    }

    ai() {
        // predict
    }

    up() {
        return (this.pos.y - this.oldY) < 0;
    }

    down() {
        return (this.pos.y - this.oldY) > 0;
    }

    draw() {
        context.fillStyle = 'white';
        context.fillRect(this.pos.x, this.pos.y, this.width, this.height);
    }

    update() {
        this.oldY = this.pos.y;
        if(keystate['w']) {
            this.pos.y -= this.vel.dy;
        } else if (keystate['a']) {
            this.pos.y += this.vel.dy;
        }

        if (this.pos.y <= 0) {
            this.pos.y = 0;
        } else if (this.pos.y >= (canvas.height - this.height)) {
            this.pos.y = (canvas.height - this.height);
        }
    }
}

// Pong object, takes a canvas
// Pong updates ball, players, court
// 

var canvas;
var context;

var ball = new Ball();
var player1, player2;
var keystate = {};

var paused = false;
var gameOver = false;

window.onload = () => {
    canvas = document.getElementById('gameCanvas');
    context = canvas.getContext('2d');

    player1 = new Player(10, canvas.height/2 - 50, 150, 20);
    player2 = new Player(canvas.width - 30, canvas.height/2 - 50, 150, 20);

    ball.pos.x = canvas.width/2;
    ball.pos.y = canvas.height/2;

    document.addEventListener('keydown', (evt) => {
        keystate[evt.key] = true;
        if (evt.key === " ") {
            paused = !paused;
        }
    });

    document.addEventListener('keyup', (evt) => {
        keystate[evt.key] = false;
    });

    draw();
    var loop = function() {
        update();
        window.requestAnimationFrame(loop);
    }
    
    window.requestAnimationFrame(loop);
};

function draw() {
    context.fillStyle = 'black';
    context.fillRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = 'white';
    context.fillText(player1.score, 100, 100);
    context.fillText(player2.score, canvas.width-100, 100);
    player1.draw();
    player2.draw();
    if (gameOver) {
        let player = (player1.score > player2.score) ? "Player 1" : "Player 2";
        context.fillText(player + " wins!", canvas.width/2, 100);
    }
    ball.draw();
}

function hit(player) {
    // if left player
    // check if ball.left < player.right
    // && ball.top < player.top && ball.bottom > player.bottom()
    if ((ball.left < player.right) && (ball.right > player.left)
    && ((ball.bottom > player.top) && (ball.top < player.bottom))) {
        return true;
    }
}

function reset() {
    player1.score = 0;
    player2.score = 0;
    player1.pos.y = canvas.width/2;
    player2.pos.y = canvas.width/2;
    ball.reset();
    gameOver = false;
}

function update() {
    if (!paused) {
        if (!gameOver) {
            ball.update();
            player1.update();

            // Player 2 AI update
            //player2.pos.y += ((player2.pos.y +  player2.height/2) < ball.pos.y) ? player2.vel.dy : -player2.vel.dy;
            if (player2.top > ball.top) {
                player2.pos.y -= player2.vel.dy;
            } else if (player2.bottom < ball.bottom) {
                player2.pos.y += player2.vel.dy;
            }

            // check if ball has hit sides
            if(ball.left > canvas.width || ball.right < 0) {
                let player = (ball.right < 0) ? player2 : player1;
                player.score++;
                if (player.score >= 10) {
                    gameOver = true;
                    paused = true;
                } else {
                    ball.reset();
                }
            }

            if (ball.top < 0 || ball.bottom > canvas.height) {
                ball.vel.dy = -ball.vel.dy;
            }

            // if ball hits player
            // is there a way to make this more general
            let player = (ball.vel.dx < 0) ? player1 : player2;
            if(hit(player)) {
                ball.vel.dx *= -1.025;
                var differenceFromMiddle = ball.pos.y - (player.pos.y + (player.height/2));
                ball.vel.dy = differenceFromMiddle * 0.20;
                //while(1) {}

                if (player.up()) {
                    ball.vel.dy *= (ball.vel.dy > 0 ? 1.35 : (-0.5));
                    if (ball.vel.dy > 0) {
                        console.log('Backspun down');
                    }
                } else if (player.down()) {
                    ball.vel.dy *= (ball.vel.dy < 0 ? 1.35 : -0.5);
                    if (ball.vel.dy < 0) {
                        console.log('Backspun up');
                    }
                }
            }
        } else {
            reset();
        }
    } 

    
    
    draw();
}