int numRings = 10;
int maxRadius;
int minRadius = 10;
int[] ringColors;
int movementDirection = 1;

void setup()
{
  size(800, 600);
  maxRadius = min(width, height) / 3;
  
  ringColors = new int[numRings];
  for (int i = 0; i < numRings; i++)
  {
    ringColors[i] = color(random(255), random(255), random(255));
  }
}

void draw()
{
  background(0);
  
  for (int i = 0; i < numRings; i++)
  {
    float radius = map(sin(frameCount * 0.02 + i * 0.3), -1, 1, minRadius, maxRadius);
    int c = ringColors[i];
    
    float x = width / 2;
    float y = height / 2;
    
    if (movementDirection == 1)
    {
      x += radius * cos(frameCount * 0.02 + i * 0.3);
    } 
    else if (movementDirection == 3)
    {
      x -= radius * cos(frameCount * 0.02 + i * 0.3);
    } 
    else if (movementDirection == 2)
    {
      y -= radius * cos(frameCount * 0.02 + i * 0.3);
    } 
    else if (movementDirection == 4)
    {
      y += radius * cos(frameCount * 0.02 + i * 0.3);
    }
    
    drawRing(x, y, radius, c);
  }
}

void keyPressed()
{
  if (key == '1')
  {
    movementDirection = 1;
  }
  else if (key == '2')
  {
    movementDirection = 2;
  }
  else if (key == '3')
  {
    movementDirection = 3;
  }
  else if (key == '4')
  {
    movementDirection = 4;
  }
  
  if (key == '+')
  {
    numRings++;
    if (numRings > 10)
    {
      numRings = 10;
    }
    numRings = max(numRings, 1);
    updateRingColors();
  }
  else if (key == '-')
  {
    numRings--;
    if (numRings < 1)
    {
      numRings = 1;
    }
    numRings = max(numRings, 1);
    updateRingColors();
  }
}

void updateRingColors()
{
  ringColors = new int[numRings];
  for (int i = 0; i < numRings; i++)
  {
    ringColors[i] = color(random(255), random(255), random(255));
  }
}

void drawRing(float x, float y, float radius, int c)
{
  noFill();
  strokeWeight(2);
  stroke(c);
  ellipse(x, y, radius * 2, radius * 2);
}
