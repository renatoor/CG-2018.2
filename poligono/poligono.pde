int n = 0;

void setup() 
{
  size(500, 500);
  textAlign(CENTER, CENTER);
  textSize(36);
  stroke(0);
}

void keyPressed()
{
  n = key - 48;
}

void draw()
{
  background(255);
  
  float r = min(width, height) * 0.45;
  float cx = width / 2;
  float cy = height / 2;

  translate(cx, cy);
  fill(255);

  for(int i = 0; i < n; i++)
  {
    float alpha1 = i * PI / (n / 2.0) - HALF_PI;
    float alpha2 = ((i != n - 1) ? i + 1 : 0) * PI / (n / 2.0) - HALF_PI;
   
    float x1 = cos(alpha1);
    float y1 = sin(alpha1);
    float x2 = cos(alpha2);
    float y2 = sin(alpha2);
    
    line(x1 * r, y1 * r, x2 * r, y2 * r);
  }
}
