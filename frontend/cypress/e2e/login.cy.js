describe('Logging into the system', () => {
  let uid
  let name

  before(function () {
    cy.fixture('user.json')
      .then((user) => {
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/users/create',
          form: true,
          body: user
        }).then((response) => {
          uid = response.body._id.$oid
          name = user.firstName + ' ' + user.lastName
        })
      })
  })

  beforeEach(function () {
    cy.visit('http://localhost:3000')
  })

  it('starting out on the loading screen', () => {
    cy.get('h1')
      .should('contain.text', 'Login')
  })

  it('email field enabled', () => {
    cy.get('.inputwrapper #email')
      .should('be.enabled')
  })

  it('log into the system with an existing account', () => {
    cy.contains('div', 'Email Address')
      .find('input[type=text]')
      .type('mon.doe@gmail.com')

    cy.get('form')
      .submit()

    cy.get('h1')
      .should('contain.text', 'Your tasks, ' + name)  
  })

  after(function () {
    cy.request({
      method: 'DELETE',
      url: `http://localhost:5000/users/${uid}`,
    }).then((response) => {
      cy.log(response.body)
    })
  })
})