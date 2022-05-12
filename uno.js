const grid =
[[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]]

let obs =
[[[2.1,0,0],
[2.15,2.1,2.1]],

[[],
[]]]


let a = [1,0,-1,0]
let b = [0,1,0,-1]
let c = [0,-1,0,1]
let d = [1,0,-1,0]

let pod = grid
let prob = pod
let LOP = []


function hit(y0,x0,z0,h0){
    for(let hy0 = 0; hy0 < h0[0]; hy0++){
        for(let hx0 = 0; hx0 < h0[1]; hx0++){
            if (y0+a[z0]*hy0+b[z0]*hx0 < 0 || y0+a[z0]*hy0+b[z0]*hx0 > 5 || x0+c[z0]*hy0+d[z0]*hx0 < 0 || x0+c[z0]*hy0+d[z0]*hx0 > 5 ){
                return false
            }
        }
    }
    return true
}

function spraw(y1,x1,z1,h1,prob1){
    for(let hy1 = 0; hy1 < h1[0]; hy1++){
        for(let hx1 = 0; hx1 < h1[1]; hx1++){
            if (prob1[y1+a[z1]*hy1+b[z1]*hx1][x1+c[z1]*hy1+d[z1]*hx1] > 3){
                return false
            }
        }
    }
    return true
}

function ca(g2,h2){
    g2 = []
    for (it of h2){
        g2.push(it)
    }
}


let n = 0
let h = [obs[n].length,obs[n][0].length]

for(let y = 0; y < 6; y++){
    for(let x = 0; x < 6; x++){
        for(let z = 0; z < 4; z++){
            if (Boolean(hit(y,x,z,h))){
                ca(prob,pod)
                for(let shy = 0; shy < h[0]; shy++){
                    for(let shx = 0; shx < h[1]; shx++){
                        prob[y+a[z]*shy+b[z]*shx][x+c[z]*shy+d[z]*shx] += obs[n][shy][shx]
                    }
                }
                if (Boolean(spraw(y,x,z,h,prob))) {
                    for(let shy = 0; shy < h[0]; shy++){
                        for(let shx = 0; shx < h[1]; shx++){
                            pod[y+a[z]*shy+b[z]*shx][x+c[z]*shy+d[z]*shx] = obs[n][shy][shx]
                        }
                    }
                    LOP.push(pod)
                    ca(pod,grid)
                }
            }
        }
    }
}

console.log(grid)