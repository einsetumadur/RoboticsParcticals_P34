  t2 = cos(phi_A);
  t3 = cos(phi_B);
  t4 = sin(phi_A);
  t5 = sin(phi_B);
  t6 = LENGTH_B*LENGTH_B;
  t11 = LENGTH_C/2.0;
  t7 = LENGTH_A*t2;
  t8 = LENGTH_A*t3;
  t9 = LENGTH_A*t4;
  t10 = LENGTH_A*t5;
  t12 = -t8;
  t13 = -t10;
  t14 = t7/2.0;
  t15 = t8/2.0;
  t16 = t9/2.0;
  t17 = t10/2.0;
  t18 = -t15;
  t19 = -t17;
  t20 = t9+t13;
  t21 = LENGTH_C+t7+t12;
  t22 = fabs(t20);
  t23 = fabs(t21);
  t26 = t16+t19;
  t29 = t11+t14+t18;
  t24 = t22*t22;
  t25 = t23*t23;
  t27 = fabs(t26);
  t30 = fabs(t29);
  t28 = t27*t27;
  t32 = t30*t30;
  t34 = t24+t25;
  t31 = -t28;
  t33 = -t32;
  t35 = 1.0/sqrt(t34);
  t36 = t6+t31+t33;
  t37 = sqrt(t36);
  A0[0][0] = t16+t17+t21*t35*t37;
  A0[1][0] = t14+t15-t20*t35*t37;
