class Object{
  float objectX;
  float objectY;
  float objectWidth;
  float objectHeight;
  color objectColor;
  float objectSpeed;
  float objectDirectionX;
  float objectDirectionY;
  String objectType; 

  Object(float _objectX, float _objectY, float _objectWidth, float _objectHeight, color _objectColor, float _objectSpeed, float _objectDirectionX, float _objectDirectionY, String _objectType) {
    objectX = _objectX;
    objectY = _objectY;
    objectWidth = _objectWidth;
    objectHeight = _objectHeight;
    objectColor = _objectColor;
    objectSpeed = _objectSpeed;
    objectDirectionX = _objectDirectionX;
    objectDirectionY = _objectDirectionY;
    objectType = _objectType;
  }

  void move() {
    objectX += objectSpeed * objectDirectionX;
    objectY += objectSpeed * objectDirectionY;
    
    if(objectType == "rect"){
      // Перевіряємо зіткнення зі стінками rect
      if (objectX <= 0 || objectX + objectWidth >= _width) {
        objectDirectionX *= -1; // Змінюємо напрямок по X
      }
      
      if (objectY <= 0 || objectY + objectHeight >= _height) {
        objectDirectionY *= -1; // Змінюємо напрямок по X
      }
    }
    else if(objectType == "ellipse"){
      // Перевіряємо зіткнення зі стінками ellipse
      if (objectX - objectWidth/2 <= 0 || objectX + objectWidth/2 >= _width) {
        objectDirectionX *= -1; // Змінюємо напрямок по X
      }
      
      if (objectY - objectHeight/2 <= 0 || objectY + objectHeight/2 >= _height) {
        objectDirectionY *= -1; // Змінюємо напрямок по X
      }
    }
  }
  
  void display() {
    fill(objectColor);
    if(objectType == "ellipse"){
      ellipse(objectX, objectY, objectWidth, objectHeight);
    }
    if(objectType == "rect"){
      rect(objectX, objectY, objectWidth, objectHeight);
    }
  }
}
