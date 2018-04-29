import Link from 'next/link'
import Head from 'next/head'
import {
  Container,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  Button } from 'reactstrap';

export default (props) => (
  <div className="wrapper">
    <Head>
      <title>Small Blog</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous" />
    </Head>
    <Navbar color="dark" dark expand="lg">
      <Link href="/" passHref>
        <NavbarBrand>Small Blog</NavbarBrand>
      </Link>
      <Nav>
        <Link href="/make-a-post" passHref>
          <NavLink>
            <Button color="success">Make a post</Button>
          </NavLink>
        </Link>
      </Nav>
    </Navbar>
    {props.children} 
  </div>
)