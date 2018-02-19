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
    }
}

class Food extends Shape{
    constructor(x = 0, y = 0) {
        super(x, y);
    }
}

class Snake extends Shape {
    constructor(x = 0, y = 0, height = 20, width = 20, speed = 20) {
        super(x, y);
        this.height = height;
        this.width = width;
        this.tail = [this.pos];
        this.last = this.tail[0];
        this.prevLast = new Position(this.last.x, this.last.y);
        this.vel = new Velocity(speed, 0);
        this.speed = speed;
    }

    draw() {
        context.fillStyle = 'white';
        for (let p of this.tail) {
            context.fillRect(p.x, p.y, this.width, this.height);
        }
    }

    update() {
        if (this.vel.dx + this.vel.dy != 0) {
            this.prevLast.x = this.last.x;
            this.prevLast.y = this.last.y;
            
            for (let i = this.tail.length-1; i > 0; i--) {
                this.tail[i].x = this.tail[i-1].x;
                this.tail[i].y = this.tail[i-1].y;
            }

            this.pos.x += this.vel.dx;
            this.pos.y += this.vel.dy;
        }
    }
}

var canvas;
var context;
var snake;
var food;
var keystate = {};
var fps, fpsInterval, startTime, now, then, elapsed;

window.onload = function() {
    console.log("Hello world!");
    canvas = document.getElementById('gameCanvas');
    context = canvas.getContext('2d');

    snake = new Snake(0, 0, 20, 20, 20);
    food = new Food(250, 250);

    // event listener
    document.addEventListener('keydown', (evt) => {
        switch(evt.key) {
            case 'w':
                if (snake.vel.dy === 0) {
                    snake.vel.dy = -(snake.speed);
                    snake.vel.dx = 0;
                }
                break;
            case 'a':
                if (snake.vel.dx === 0) {
                    snake.vel.dx = -(snake.speed);
                    snake.vel.dy = 0;
                }
                break;
            case 's':
                if (snake.vel.dy === 0) {
                    snake.vel.dy = snake.speed;
                    snake.vel.dx = 0;
                }
                break;
            case 'd':
                if (snake.vel.dx === 0) {
                    snake.vel.dx = snake.speed;
                    snake.vel.dy = 0;
                }
                break;
            case ' ':
                snake.vel.dx = 0;
                snake.vel.dy = 0;
        }
    });

    fps = 15;
    fpsInterval = 1000 / fps;
    then = Date.now();
    startTime = then;


    draw();
    var loop = function() {
        window.requestAnimationFrame(loop);

        now = Date.now();
        elapsed = now - then;

        if (elapsed > fpsInterval) {
            then = now - (elapsed % fpsInterval);

            update();
            draw();
        }
    }

    window.requestAnimationFrame(loop);
}

function draw() {
    context.fillStyle = 'black';
    context.fillRect(0, 0, canvas.width, canvas.height);

    if (food) {
        drawFood();
    } else {
        let newx = getRandomInt(10, 490);
        while (newx % 10 != 0 || newx % 20 == 0) {
            newx = getRandomInt(10, 490);
        }

        let newy = getRandomInt(10, 490);
        while (newy % 10 != 0 || newy % 20 == 0) {
            newy = getRandomInt(10, 490);
        }

        food = new Food(newx, newy);
    }

    drawSnake();
}

function drawFood() {
    context.fillStyle = 'white';
    context.beginPath();
    context.arc(food.pos.x, food.pos.y, 10, 0, Math.PI*2, true);
    context.fill();
}

function drawSnake() {
    // context.fillStyle = 'white';
    // context.fillRect(snake.pos.x, snake.pos.y, snake.width, snake.height);

    context.fillStyle = 'white';
    for (let p of snake.tail) {
        context.fillRect(p.x, p.y, snake.width, snake.height);
    }
}

function update() {
    snake.update();

    collide();

    // check if snake position is in tile of food, 240,240
    if (food) {
        let foodPos = new Position(food.pos.x - 10, food.pos.y - 10);

        if ((foodPos.x === snake.pos.x) && (foodPos.y === snake.pos.y)) {
            food = null;
            snake.tail.push(new Position(snake.prevLast.x, snake.prevLast.y));
            snake.last = snake.tail[snake.tail.length-1];
        }
    }

    

    if (snake.pos.x >= canvas.width) {
        snake.pos.x = 0;
    } else if (snake.pos.x < 0) {
        snake.pos.x = canvas.width-20;
    }

    if (snake.pos.y >= canvas.height) {
        snake.pos.y = 0;
    } else if (snake.pos.y < 0) {
        console.log(snake.pos.y);
        snake.pos.y = canvas.height-20;
    }
}

function collide() {
    let pos = snake.pos;
    for(let i = 1; i < snake.tail.length; i++) {
        if (pos.x === snake.tail[i].x && pos.y === snake.tail[i].y) {
            console.log('touched');
            snake.tail.splice(1);
            break;
        }
    }

}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
  }