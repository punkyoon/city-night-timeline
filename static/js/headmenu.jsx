import React, { Component } from 'react'
import { Menu, Segment } from 'semantic-ui-react'

export default class headmenu extends Component {
  state = { activeItem: 'MAIN' }

  handleItemClick = (e, { name }) => this.setState({ activeItem: name })

  render() {
    const { activeItem } = this.state

    return (
      <div>
        <Menu pointing secondary>
          <Menu.Item name='MAIN' active={activeItem === 'MAIN'} onClick={this.handleItemClick} />
          <Menu.Item name='SEARCH' active={activeItem === 'SEARCH'} onClick={this.handleItemClick} />
        </Menu>
      </div>
    )
  }
}

export default headmenu
