void orbita(float dt, float at, float psx, float psy, float dl, float al) 
{
  float ptx = dt * cos(at) + psx;
  float pty = dt * sin(at) + psy;
  
  ellipse(ptx, pty, 60, 60);
  
  float plx = dl * cos(al) + ptx;
  float ply = dl * sin(al) + pty;
  
  ellipse(plx, ply, 30, 30);
}

void setup() 
{
  size(1000, 1000);
  stroke(0);
}
int n = 0;
void draw()
{
  background(200);
 
  float r = min(width, height) * 0.45;
  float cx = width / 2;
  float cy = height / 2;

  float at = 0;
  
  translate(cx, cy);
  fill(255);
  ellipse(0, 0, 120, 120);

  float mult = 0.005;

  at = (millis() * mult) * PI / 30 - HALF_PI;

  n = (++n) % 60;

  float al = ((millis() * mult) + n) * PI / 30 - HALF_PI;
  orbita(r, at, 0, 0, 80, al);
}
