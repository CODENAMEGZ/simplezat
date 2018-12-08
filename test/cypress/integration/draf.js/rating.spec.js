context('Rating', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000')
  })
  it('should be able to give positive rating with comment', () => {
    cy.contain('How do we do?')
        cy.get('imag').should('have.attr', 'alt', 'Postive')
        cy.get('imag').should('have.attr', 'alt', 'Neutral')
        cy.get('imag').should('have.attr', 'alt', 'Negative')

        cy.get('img[alt="Positive"]').click()
        cy.wait(1000)

        cy.contain('Any comment?')
        cy.get('input[name="comment"]').type('You are doing great!') 
        cy.get('button'.slack)

        cy.contain('Thank you!')
      })    
})