
phi_A = sym("phi_A", "real");
phi_B  = sym("phi_B", "real");
LENGTH_A = sym("LENGTH_A", "real");
LENGTH_B = sym("LENGTH_B", "real");
LENGTH_C = sym("LENGTH_C", "real");
F_x = sym("F_x", "real");
F_y = sym("F_y", "real");

P_1 = [LENGTH_A * sin(phi_A); LENGTH_C/2 - LENGTH_A * cos(phi_A)];
P_2 = [LENGTH_A * sin(phi_B); -LENGTH_C/2 - LENGTH_A * cos(phi_B)];
v_12 = P_2 - P_1;
P_M = (P_1 + P_2) / 2;
n = [-v_12(2); v_12(1)];
n = n / norm(n);
alpha = sqrt(LENGTH_B^2 - 1/4 * dot(v_12, v_12));
P = P_M + alpha * n;
ccode(P)

J = [diff(P(1), phi_A), diff(P(1), phi_B);
     diff(P(2), phi_A), diff(P(2), phi_B)];
tau = J' * [F_x; F_y];
ccode(tau)

tau_val = subs(tau, ...
    [LENGTH_A, LENGTH_B, LENGTH_C, F_x, F_y, phi_A, phi_B], ...
    [60, 100, 100, -1, 1, 2*pi/3, pi/3]);
vpa(tau_val)
