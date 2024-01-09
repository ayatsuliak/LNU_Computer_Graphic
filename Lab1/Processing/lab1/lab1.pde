int _width = 800;
int _height = 600;

int collisions = 0; 

ArrayList<Ball> balls = new ArrayList<Ball>();
ArrayList<Object> objects = new ArrayList<Object>();

Object object1 = new Object(60, 65, 60, 40, color(0, 0, 250), 4, 1, 0, "ellipse");
Object object2 = new Object(500, 356, 50, 70, color(0, 250, 0), 3, 0, 1, "ellipse");
Object object3 = new Object(320, 650, 220, 220, color(100, 100, 100), 0, 0, 0, "ellipse");
Object object4 = new Object(100, 200, 200, 150, color(0, 0, 0), 0, 0, 0, "rect");
{objects.add(object1);
objects.add(object2);
objects.add(object3);
objects.add(object4);
}


void setup(){
  size(_width, _height, P2D);
  noStroke();
  fill(0);
}

void draw(){
  background(250);  
  
  for (Object obj : objects) {
    obj.move();
    obj.display();
  }
  
  // Рух і відображення кульок
  for (Ball ball : balls) {
    ball.move();
    ball.display();
    for (Object obj : objects) {
      ball.checkCollisionWithObject(obj);
    }
  }  
  // Виводимо кількість зіткнень на екран
  textSize(20);
  fill(0);
  text("Зіткнень: " + collisions, 10, height - 10);
}

void mousePressed() {
  if (mouseButton == LEFT) {
    // Додавання нової кульки за координатами мишки
    float x = mouseX;
    float y = mouseY;
    color ballColor = color(random(255), random(255), random(255)); // Випадковий колір
    Ball newBall = new Ball(x, y, 20, ballColor, 6, random(-1, 1), random(-1, 1)); // Створення нової кульки
    balls.add(newBall); // Додавання кульки до списку
  } else if (mouseButton == RIGHT && balls.size() > 1) {
    // Видалення останньої кульки, якщо їх більше однієї
    balls.remove(balls.size() - 1);
  }
}

//добре розібратись в коді
