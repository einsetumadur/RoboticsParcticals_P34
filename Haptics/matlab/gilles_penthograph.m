clc
clear 
%% practical haptics
a = 102;
b = 111;
c = 60;

%% 7.2 1B
phia = pi/2;
phib = 0;
P1 = a*[sin(phia);cos(phia)] + [0;c/2]; 
P2 = a*[sin(phib);cos(phib)] - [0;c/2]; 
PM = (P1+P2)./2;
vPMP = [-(P2(2)-P1(2)); P2(1)-P1(1)];
nvPMP = norm(vPMP,2);
nPMP = sqrt(b^2-norm(P1-PM, 2)^2);
P = vPMP.*(nPMP/nvPMP) + PM

%% 7.2 1C
syms phi_A phi_B LENGTH_A LENGTH_B LENGTH_C real
P1 = LENGTH_A*[sin(phi_A);-cos(phi_A)] + [0;LENGTH_C/2]; 
P2 = LENGTH_A*[sin(phi_B);-cos(phi_B)] - [0;LENGTH_C/2]; 
PM = (P1+P2)./2;
vPMP = [-(P2(2)-P1(2)); P2(1)-P1(1)];
nvPMP = norm(vPMP,2);
nPMP = sqrt(LENGTH_B^2-norm(P1-PM, 2)^2);
P = vPMP.*(nPMP/nvPMP) + PM;
fwcode = ccode(simplyfy(P),'File','./penthofwkin.c');

%% 7.2 2B
syms F_x F_y real
J = jacobian(P,[phi_A,phi_B]);
Torques = J'*[F_x;F_y];
J = simplify(J);
bcincode = ccode(Torques,'File','./pentho_backcin.c');

%%
solve(diff(inv(J')) == [0,0]) 


