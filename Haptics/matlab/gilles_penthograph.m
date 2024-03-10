clc
clear 
%% practical haptics
a = 102;
b = 111;
c = 60;

%% 7.2 1B
phia = pi/2
phib = pi/2
P1 = a*[sin(phia);cos(phia)] + [0;c/2]; 
P2 = a*[sin(phib);cos(phib)] - [0;c/2]; 
PM = (P1+P2)./2;
nPM = norm(PM,2);
PmP = sqrt(b^2 -((a*sin(phia) - a*sin(phib))/2)^2 -((a*cos(phia) - a*cos(phib) - c)/2)^2);
P = PM.*(PmP/nPM) + PM

%% 7.2 1C
syms phi_A phi_B LENGTH_A LENGTH_B LENGTH_C
P1 = LENGTH_A*[sin(phi_A);cos(phi_A)] + [0;LENGTH_C/2]; 
P2 = LENGTH_A*[sin(phi_B);cos(phi_B)] - [0;LENGTH_C/2]; 
PM = (P1+P2)./2;
nPM = norm(PM,2);
PmP = sqrt(LENGTH_B^2 -((LENGTH_A*sin(phi_A) - LENGTH_A*sin(phi_B))/2)^2 ...
      -((LENGTH_A*cos(phi_A) - LENGTH_A*cos(phi_B) - LENGTH_C)/2)^2);
P = PM.*(PmP/nPM) + PM;
fwcode = ccode(P,'File','./penthofwkin.c');

%% 7.2 2B
syms F_x F_y
J = jacobian(P,[phi_A,phi_B]);
Torques = J'*[F_x;F_y];
bcincode = ccode(Torques,'File','./pentho_backcin.c');


