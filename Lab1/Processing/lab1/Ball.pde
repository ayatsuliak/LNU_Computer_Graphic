class Ball {
  float ballX;
  float ballY;
  float ballSize;
  color ballColor;
  float ballSpeed;
  float ballDirectionX;
  float ballDirectionY;

  Ball(float _ballX, float _ballY, float _ballSize, color _ballColor, float _ballSpeed, float _ballDirectionX, float _ballDirectionY) {
    ballX = _ballX;
    ballY = _ballY;
    ballSize = _ballSize;
    ballColor = _ballColor;
    ballSpeed = _ballSpeed;
    ballDirectionX = _ballDirectionX;
    ballDirectionY = _ballDirectionY;
  }

  void move() {
    ballX += ballSpeed * ballDirectionX;
    ballY += ballSpeed * ballDirectionY;
    
    // Перевіряємо зіткнення зі стінками
    if (ballX - ballSize/2 <= 0 || ballX + ballSize/2 >= _width) {
      ballDirectionX *= -1; // Змінюємо напрямок по X
      collisions++;
    }
    if (ballY - ballSize/2<= 0 || ballY + ballSize/2 >= _height) {
      ballDirectionY *= -1; // Змінюємо напрямок по Y
      collisions++;
    }
    
    // Перевірка відбиття від інших кульок
    for (Ball other : balls) {
      if (other != this) { // Перевірка на колізію із іншими кульками (крім самої себе)
        float distance = dist(ballX, ballY, other.ballX, other.ballY);
        if (distance < ballSize / 2 + other.ballSize / 2) {
          // Відбивання від іншої кульки
          float angle = atan2(ballY - other.ballY, ballX - other.ballX);
          ballDirectionX = cos(angle);
          ballDirectionY = sin(angle);
          collisions++;
        }
      }
    }
    // Перевіряємо, чи кулька попала в вершину екрану і зупиняємо її рух
    if (ballY - ballSize/2 <= 0 && ballX - ballSize/2 <= 0 || ballY + ballSize/2 >= _height && ballX - ballSize/2 <= 0 || ballY + ballSize/2 >= _height && ballX + ballSize/2 >= _width || ballY - ballSize/2 <= 0 && ballX + ballSize/2 >= _width) {
      noLoop();
    }
  }
  
  void display() {
    fill(ballColor);
    ellipse(ballX, ballY, ballSize, ballSize);
  }
  
  void checkCollisionWithObject(Object obj) {
    float dx = obj.objectX - ballX;
    float dy = obj.objectY - ballY;
    float angleOfIncidence = atan2(dy, dx);
    float angleOfReflection = angleOfIncidence + PI;
    if(obj.objectType == "rect"){
      //Перевірка відбиття кульки від прямокутника
      if (ballX + ballSize/2 >= obj.objectX && ballX - ballSize/2 <= obj.objectX + obj.objectWidth &&
          ballY + ballSize/2 >= obj.objectY && ballY - ballSize/2 <= obj.objectY + obj.objectHeight) {
        // Відбиття кульки від прямокутника
        if (ballX < obj.objectX || ballX > obj.objectX + obj.objectWidth) {
          ballDirectionX *= -1; // Змінюємо напрямок по X
          collisions++;
        }
        if (ballY < obj.objectY || ballY > obj.objectY + obj.objectHeight) {
          ballDirectionY *= -1; // Змінюємо напрямок по Y
          collisions++;
        }
      }
    }
    else if(obj.objectType == "ellipse"){  
      float distance = dist(ballX, ballY, obj.objectX, obj.objectY);
      
      if (obj.objectDirectionX == 0 && obj.objectDirectionY == 0) {
        // Якщо об'єкт не рухається
        if (distance < (ballSize / 2 + max(obj.objectWidth, obj.objectHeight) / 2)) {
          // Відбиття кульки
          ballDirectionX = cos(angleOfReflection);
          ballDirectionY = sin(angleOfReflection);
          collisions++;
        }
      } else if (obj.objectDirectionX == 0) {
        // Якщо об'єкт рухається вертикально
        if (distance < (ballSize / 2 + obj.objectHeight / 2)) {
          // Відбиття кульки
          ballDirectionX = cos(angleOfReflection);
          ballDirectionY = sin(angleOfReflection);
          collisions++;
        }
      } else if (obj.objectDirectionY == 0) {
        // Якщо об'єкт рухається горизонтально
        if (distance < (ballSize / 2 + obj.objectWidth / 2)) {
          // Відбиття кульки
          ballDirectionX = cos(angleOfReflection);
          ballDirectionY = sin(angleOfReflection);
          collisions++;
        }
      } else {
        // Якщо об'єкт рухається в обидва напрямки
        if (distance < (ballSize / 2 + max(obj.objectWidth, obj.objectHeight) / 2)) {
          // Відбиття кульки
          ballDirectionX = cos(angleOfReflection);
          ballDirectionY = sin(angleOfReflection);
          collisions++;
        }
      }
    }
  }
}
