void setup() 
{
  size(500, 500);
  textAlign(CENTER, CENTER);
  textSize(36);
  stroke(0);
}

void draw()
{
  background(200);
 
  float r = min(width, height) * 0.45;
  float cx = width / 2;
  float cy = height / 2;
  
  translate(cx, cy);
  fill(255);
  ellipse(0, 0, 2 * r, 2 * r);

  float tt = 20; // tamanho do traco das horas
  float tm = 10; // tamanho do traco dos minutos

  for(int i = 0; i < 60; i++)
  {
    float alpha = i * PI / 30 - HALF_PI;
    float x = cos(alpha);
    float y = sin(alpha);

    if(i % 5 != 0)
    { 
      line(x * (r - tm), y * (r - tm), x * r, y * r);
    }
    else
    {
      fill(0);
  
      if(i == 0)
      {
       text("12", x * (r - tt), y * (r - tt));
      }
      else
      {
         text((i / 5) + "", x * (r - tt), y * (r - tt));
      }

      line(x * (r - tt), y * (r - tt), x * r, y * r);
    }
    
    float min_alpha = (i + (second() / 60.0)) * PI / 30 - HALF_PI;
    float min_x = cos(min_alpha);
    float min_y = sin(min_alpha);
    
    float hour_alpha = (i + (5 * (minute() / 60.0))) * PI / 30 - HALF_PI;
    float hour_x = cos(hour_alpha);
    float hour_y = sin(hour_alpha);
    
    if((hour() % 12) * 5 == i) line(hour_x, hour_y, hour_x * (r * 0.65), hour_y * (r * 0.65));
    if(minute() == i)          line(min_x, min_y, min_x * (r * 0.9), min_y * (r * 0.9));
    if(second() == i)          line(x, y, x * r, y * r);
  }
}
