class HMM{
   float[][] A;
   float[][] B;
   float[] Pi;
   int[] O;
   int[] V;
   int N;
   int M;
   int T;
}

class BaumWelch {
   public static HMM main(String args[]) {
   
      int N = #; //  |U|
      int M = #; //  |V|
      int T = #; //  |Q| and |O|
      int[] o = {#,#,...}; //  observation string
      int[] v = {#,#,...}; //  observation space
      float[] pi = new float[N]; //  create initial guesses
      float[][] a = new float[N][N];
      float[][] b = new float[N][M];
      float epsilon = #; //  threshold for stopping algorithm
      
      HMM lambda = new HMM();
      lambda.A = a;
      lambda.B = b;
      lambda.Pi = pi;
      lambda.O = o;
      lambda.N = N;
      lambda.M = M;
      lambda.T = T;
      lambda.V = v;
      HMM lambdaTilde = new HMM();
      
      //Update Lambda with Baum Welch variables until
      // 1 - (P(O|Lambda)/P(O|Lambda-tilde)) is less than epsilon:

      int z=0;
      while (z=0){
         lambdaTilde = update(lambda);
         if( 1 - (prob(lambda)/prob(lambdaTilde)) < epsilon ){
            lambda = lambdaTilde;
         }
         else{
            z=1;
            return lambdaTilde;
         }
      }
   }
   
   public static HMM update(HMM L){
      HMM Lnew = new HMM();
      Lnew.A = newA(L);
      Lnew.B = newB(L);
      Lnew.Pi = newPi(L);
      Lnew.O = L.O;
      Lnew.N = L.N;
      Lnew.M = L.M;
      Lnew.T = L.T;
      Lnew.V = L.V;
      return Lnew;
   }
      
   public static float[][] makeAlpha(HMM L) {
      float[][] aa = L.A;
      float[][] bb = L.B;
      float[] pp = L.Pi;
      int[] oo = L.O;
      int N = L.N;
      int T = L.T;
      float[][] alpha = new float[N][T];
      for(int j=0; j<N; j++){
         alpha[j][0] = pp[j] * bb[j][oo[0]];
      }
      for(int t=1; t<T; t++){
         for(int j=0; j<N; j++){
            float old = 0;
            for(int i=0; i<N; i++){
               alpha[j][t] = old + (alpha[i][t-1] * aa[i][j] * bb[j][oo[t]]);
               //wl+cs
               old = alpha[j][t];
            }
         }
      }
      return alpha;
   }
      
   public static float[][] makeBeta(HMM L) {
      float[][] aa = L.A;
      float[][] bb = L.B;
      float[] pp = L.Pi;
      int[] oo = L.O;
      int N = L.N;
      int T = L.T;
      float[][] beta = new float[N][T];
      for(int i=0; i<N; i++){
         beta[i][T-1] = 1;
      }
      for(int t = (T-2); t>=0; t--){
         for(int i=0; i<N; i++){
            float old = 0;
            for(int j=0; j<N; j++){
               beta[i][t] = old + (beta[j][t+1] * aa[i][j] * bb[j][oo[t+1]]);
               old = beta[i][t];
            }
         }
      }
      return beta;
   }

   public static float[][] makeGamma(HMM L) {
      float[][] aa = L.A;
      float[][] bb = L.B;
      float[] pp = L.Pi;
      int[] oo = L.O;
      int N = L.N;
      int T = L.T;
      float[][] alpha = makeAlpha(L);
      float[][] beta = makeBeta(L);
      float[][] gamma = new float[N][T];
      float sum, old;
      for(int i=0; i<N; i++){
         for(int t=0; t<T; t++){
            old = 0;
            sum = 0;
            for(int j=0; j<N; j++){
               sum = old + (alpha[j][t] * beta[j][t]);
               old = sum;
            }
            gamma[i][t] = (alpha[i][t] * beta[i][t]) / sum;
         }
      }
      return gamma;
   }

   public static float[][][] makeXi(HMM L){
      float num, den, old;
      num = 0;
      den = 0;
      float[][] alpha = makeAlpha(L);
      float[][] beta = makeBeta(L);
      float[][] a = L.A;
      float[][] b = L.B;
      int[] o = L.O;
      int N = L.N;
      int T = L.T;
      float[][][] xi = new float[N][N][T];
      for(int i=0; i<N; i++){
         for(int j=0; j<N; j++){
            for(int t=0; t<(T-1); t++){
               num = alpha[i][t] * a[i][j] * beta[j][t+1] * b[j][o[t+1]];
               old = 0;
               for(int x=0; x<N; x++){
                  for(int y=0; y<N; y++){
                     den = old + alpha[x][t] * a[x][y] 
                                * beta[y][t+1] * b[y][o[t+1]];
                     old = den;
                  }
               }
               xi[i][j][t] = num / den;
            }
         }
      }
      return xi;
   }

   public static float prob(HMM L){
      //Computes the probability P(O|Lambda)
      int N, T;
      float old, PO;
      float[][] alpha = makeAlpha(L);
      N = L.N;
      T = L.T -1;
      old = 0;
      PO = 0;
      for(int i=0; i<N; i++){
         PO = old + alpha[i][T];
         old = PO;
      }
      return PO;
   }

   //The Baum-Welch update variables:
   public static float[] newPi(HMM L){
      int N;
      N = L.N;
      float[] pinew = new float[N];
      float[][] gamma = makeGamma(L);
      for(int i=0; i<N; i++){
         pinew[i] = gamma[i][1];
      }
      return pinew;
   }

   public static float[][] newA(HMM L){
      int N, T;
      float old, old2, num, den, sum;
      float[][] gamma = makeGamma(L);
      float[][][] xi = makeXi(L);
      N = L.N;
      float[][] anew = new float[N][N];
      T = L.T;
      num = 0;
      den = 0;
      for(int i=0; i<N; i++){
         for(int j=0; j<N; j++){
            old = 0;
            old2 = 0;
            for(int t=0; t<(T-1); t++){
               num = old + xi[i][j][t];
               old = num;
               den = old2 + gamma[i][t];
               old2 = den;
            }
            anew[i][j] = num / den;
         }
      }            
      return anew;
   }
   
   public static float[][] newB(HMM L){
      int N, M, T;
      float den, num, old, old2;
      int[] o = L.O;
      int[] v = L.V;
      N = L.N;
      M = L.M;
      T = L.T;
      float[][] gamma = makeGamma(L);
      float[][] bnew = new float[N][M];
      den = 0;
      num = 0;
      for(int i=0; i<N; i++){
         for(int j=0; j<M; j++){
            old = 0;
            old2 = 0;
            for(int t=1; t<T; t++){
               if (o[t] == v[j]){
                  num = old + gamma[i][t];
                  old = num;
               }
               den = old2 + gamma[i][t];
               old2 = den;
            }
            bnew[i][j] = num / den;
         }
      }
      return bnew;
   }
}