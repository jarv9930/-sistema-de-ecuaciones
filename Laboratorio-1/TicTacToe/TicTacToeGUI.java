import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

import javax.swing.*;

public class TicTacToeGUI extends JFrame implements ActionListener{
    private JButton[] btTicTac;
    private JLabel winner;
    private JButton restartButton; // Botón para reiniciar el juego
    private int turn = 0; // Para controlar el turno de los jugadores
    private ImageIcon iconCruz, iconCirculo, iconCasilla;
    private JButton btnHumanVsComputer;
    private JButton btnComputerVsComputer;
    private JPanel modeSelectionPanel;
    private boolean isComputerVsComputer = false; // Para controlar el modo de juego
    private boolean gameEnded = false;

    public TicTacToeGUI() {
        this.setTitle("Tic Tac Toe");
        this.setSize(800, 800);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        loadIcons();
        initModeSelection();
        this.setVisible(true);
    }

    private void loadIcons() {
        iconCruz = new ImageIcon(new ImageIcon(getClass().getResource("/iconos/cruz.png")).getImage().getScaledInstance(120, 120, Image.SCALE_SMOOTH));
        iconCirculo = new ImageIcon(new ImageIcon(getClass().getResource("/iconos/circulo.png")).getImage().getScaledInstance(120, 120, Image.SCALE_SMOOTH));
        iconCasilla = new ImageIcon(new ImageIcon(getClass().getResource("/iconos/casilla.png")).getImage().getScaledInstance(150, 150, Image.SCALE_SMOOTH));
    }

    private void initModeSelection() {
        modeSelectionPanel = new JPanel(new GridLayout(1, 2));
        btnHumanVsComputer = new JButton("Humano vs Computadora");
        btnComputerVsComputer = new JButton("Computadora vs Computadora");

        btnHumanVsComputer.addActionListener(e -> startGame(false));
        btnComputerVsComputer.addActionListener(e -> startGame(true));

        modeSelectionPanel.add(btnHumanVsComputer);
        modeSelectionPanel.add(btnComputerVsComputer);

        this.getContentPane().add(modeSelectionPanel, BorderLayout.NORTH);

        pack(); // Ajusta el tamaño de la ventana basado en los componentes
    }
    
    private void startGame(boolean computerVsComputer) {
        this.getContentPane().removeAll(); // Elimina todos los componentes
        this.isComputerVsComputer = computerVsComputer;

        initComponents();
        if (computerVsComputer) {
            computerVsComputerGame();
        }

    }
    private void initComponents() {
        JPanel panel = new JPanel(new GridLayout(3, 3));
        panel.setPreferredSize(new Dimension(450, 450));
        btTicTac = new JButton[9];
        for (int i = 0; i < 9; i++) {
            btTicTac[i] = new JButton(iconCasilla);
            btTicTac[i].addActionListener(this);
            panel.add(btTicTac[i]);
        }
        winner = new JLabel("Ganador: ", SwingConstants.CENTER);
        restartButton = new JButton("Reiniciar Juego");
        restartButton.addActionListener(e -> restartGame());

        this.getContentPane().setLayout(new BorderLayout());
        this.getContentPane().add(panel, BorderLayout.CENTER);
        this.getContentPane().add(winner, BorderLayout.NORTH);
        this.getContentPane().add(restartButton, BorderLayout.SOUTH);
        this.pack();
        // Centra el JFrame en la pantalla
        this.setLocationRelativeTo(null);
        this.revalidate();
        this.repaint();
    }
    
    private void restartGame() {
        gameEnded = false;
        turn = 0;
        winner.setText("Ganador: ");
        for (JButton button : btTicTac) {
            button.setIcon(iconCasilla);
            button.setEnabled(true);
        }
        if (isComputerVsComputer) {
            computerVsComputerGame();
        }
    }

    private void computerVsComputerGame() {
        Timer timer = new Timer(500, e -> {
            computerMove();
            if (turn >= 9 || !winner.getText().equals("Ganador: ")) {
                ((Timer) e.getSource()).stop();
            }
        });
        timer.start();
    }

    private void computerMove() {
        if (gameEnded) return;
        ArrayList<Integer> availableSpaces = new ArrayList<>();
        for (int i = 0; i < btTicTac.length; i++) {
            if (btTicTac[i].getIcon().equals(iconCasilla)) {
                availableSpaces.add(i);
            }
        }
        if (!availableSpaces.isEmpty()) {
            int move = availableSpaces.get((int) (Math.random() * availableSpaces.size()));
            if (turn % 2 == 0) {
                btTicTac[move].setIcon(iconCruz); 
            } else {
                btTicTac[move].setIcon(iconCirculo);
            }
            turn++;
            checkForWinner();
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (gameEnded) return;
        JButton buttonClicked = (JButton) e.getSource();
        if (buttonClicked.getIcon().equals(iconCasilla) && turn < 9) {
            if (turn % 2 == 0) {
                buttonClicked.setIcon(iconCruz);
                turn++;
                checkForWinner();
            }

            if (turn < 9) {
                Timer timer = new Timer(400, event -> {
                    computerMove();
                    checkForWinner();
                });
                timer.setRepeats(false); // Asegura de que el Timer se ejecute solo una vez
                timer.start();
            }
        }
    }


    private void checkForWinner() {
        for (int[] winPosition : new int[][]{{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}}) {
            if (checkWinCondition(winPosition)) {
                String winnerText = turn % 2 == 0 ? "Gana Círculo!" : "Gana Cruz!";
                winner.setText(winnerText);
                gameEnded = true;
                //disableButtons();
                return;
            }
        }

        if (turn == 9) {
            winner.setText("Ganador: Empate");
            gameEnded = true;
        }
    }
    private boolean checkWinCondition(int[] positions) {
        Icon first = btTicTac[positions[0]].getIcon();
        return first != iconCasilla && first == btTicTac[positions[1]].getIcon() && first == btTicTac[positions[2]].getIcon();
    }
    

    private boolean checkPattern(String pattern) {
        int a = pattern.charAt(0) - '0';
        int b = pattern.charAt(1) - '0';
        int c = pattern.charAt(2) - '0';

        if (!btTicTac[a].getIcon().equals(iconCasilla) && 
            btTicTac[a].getIcon().equals(btTicTac[b].getIcon()) && 
            btTicTac[a].getIcon().equals(btTicTac[c].getIcon())) {
            return true;
        }
        return false;
    }

    private void disableButtons() {
        for (JButton button : btTicTac) {
            button.setEnabled(false);
        }
    }

    public static void main(String[] args) {
        new TicTacToeGUI();
    }
}
