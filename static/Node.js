function Node(data) {
    this.pos = createVector(width/2, height/2)
    this.id = data.id
    this.w = data.w
    this.data = data
    this.edges = []
    this.size = 75
}

Node.prototype.show = function() {
    fill(255)
    strokeWeight(3)
    noStroke()
    if (currentNode == this.id) {
        stroke(50,255,50)
    }
    ellipse(this.pos.x, this.pos.y, this.size)
    noStroke()
    textSize(20)
    fill(80, 150, 255)
    text(this.id, this.pos.x + 40, this.pos.y - this.size + 40)
    textSize(32)
    fill(50)
    text(this.w, this.pos.x, this.pos.y)
}

Node.prototype.intersects = function(x, y) {
    return (dist(x, y, this.pos.x, this.pos.y) - this.size) <= 0
}

let currentNode = 1