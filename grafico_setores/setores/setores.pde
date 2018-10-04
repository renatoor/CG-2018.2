float valores [] = new float [] {10.0, 15.0, 8.0, 20.0};

color paleta [] = new color[] {
    color(255,0,0),
    color(255,128,0),
    color(255,255,0),
    color(0,255,0)
  };

void setup() 
{
  size(100,100);
  textAlign(CENTER,CENTER);
  textSize(36);
  stroke(0);
}

void draw()
{
  float total = 0;
  float angulo = 0;
  float soma = 0;
  
  for(int i=0; i< valores.length; i++){
    total += valores[i];
  }
  
  for(int i=0; i< valores.length; i++){
      soma += (valores[i] / total) * TWO_PI;
      fill(paleta[i]);
      arc(50, 55, 60, 60, angulo, soma, PIE);
      angulo = soma;
  }
}
